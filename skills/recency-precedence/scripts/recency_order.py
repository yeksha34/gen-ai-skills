#!/usr/bin/env python3
"""Order a story's reference sources from oldest to newest, so newer text can override older.

Usage:
  python recency_order.py <story_root> [--extra <memory_dir>] [--paths lore rules characters]
  python recency_order.py <story_root> --term "old name" "new name" [--extra <memory_dir>]
         [--exclude chapters/ drafts/] [--since 2026-10-20] [--width 200]
  python recency_order.py <story_root> --lines lore/<file>.md

Modes:
  (default)  every text file under <story_root> (and each --extra dir), oldest first
  --term     a timeline of every line that mentions any of the terms, oldest first,
             each line dated by git blame (its own last change), not by its file
  --lines    one file's lines grouped into ranges by the commit that last changed them

Nothing is hard-coded: files are discovered on every run. A date says when text was
last touched, not that every idea in it was revised then; blame lines carry the commit
subject so you can tell a decision from a mechanical pass.

Date sources, labelled in the output:
  git        last commit touching the file / line
  explicit   a later ISO date written in the text itself ("on 2026-10-28 ...")
  modified   a `modified:` / `updated:` frontmatter field (files outside git; memory)
  mtime      filesystem time, only for untracked files with no `modified:` field;
             it moves when a file is merely re-saved, so it is the weakest signal
  none       untracked and undated; sorted as oldest
Times are compared in UTC to the minute, so same-day sources still order correctly.
"""
import argparse
import datetime as dt
import re
import subprocess
import sys
from pathlib import Path

TEXT_EXT = {".md", ".txt", ".markdown", ".yaml", ".yml", ".json", ".rst", ".fountain"}
FM_DATE = re.compile(r"^\s*(?:modified|updated|last_updated|date):\s*['\"]?(\d{4}-\d{2}-\d{2}(?:[T ]\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?(?:Z|[+-]\d{2}:?\d{2})?)?)", re.M)
ISO_DATE = re.compile(r"\b(20\d{2}-[01]\d-[0-3]\d)\b")


def utc(when: dt.datetime) -> str:
    """Minute-precision UTC stamp; naive times are taken as local."""
    if when.tzinfo is None:
        when = when.astimezone()
    return when.astimezone(dt.timezone.utc).strftime("%Y-%m-%d %H:%M")


def parse_stamp(text: str) -> str:
    text = text.replace(" ", "T").replace("Z", "+00:00")
    try:
        return utc(dt.datetime.fromisoformat(text))
    except ValueError:
        return text[:10] + " 00:00"


def git(repo: Path, *args: str) -> str:
    r = subprocess.run(["git", "-C", str(repo), *args], capture_output=True,
                       text=True, encoding="utf-8", errors="replace")
    return r.stdout if r.returncode == 0 else ""


def repo_root(path: Path) -> Path | None:
    out = git(path, "rev-parse", "--show-toplevel").strip()
    return Path(out) if out else None


def discover(root: Path):
    for p in sorted(root.rglob("*")):
        if p.is_file() and p.suffix.lower() in TEXT_EXT and ".git" not in p.parts:
            yield p


def last_touch(repo: Path, root: Path) -> dict[str, tuple[str, str]]:
    """repo-relative path -> (stamp, subject) of the newest commit touching it."""
    rel = root.resolve().relative_to(repo.resolve()).as_posix() or "."
    out = git(repo, "log", "--format=@@%aI\t%s", "--name-only", "--", rel)
    seen, cur = {}, None
    for line in out.splitlines():
        if line.startswith("@@"):
            when, subj = line[2:].split("\t", 1)
            cur = (parse_stamp(when), subj)
        elif line.strip() and cur:
            seen.setdefault(line.strip(), cur)
    return seen


def file_date(p: Path, repo: Path | None, touched: dict, today: str):
    text = p.read_text(encoding="utf-8", errors="replace")
    head = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
    fm = FM_DATE.search(head.group(1)) if head else None
    inline = [d for d in ISO_DATE.findall(text) if d <= today]
    key = p.resolve().relative_to(repo.resolve()).as_posix() if repo else None

    if key in touched:
        date, src = touched[key][0], "git"
    elif fm:  # a written stamp beats mtime, which moves on any re-save
        date, src = parse_stamp(fm.group(1)), "modified"
    elif repo is None:
        date, src = utc(dt.datetime.fromtimestamp(p.stat().st_mtime)), "mtime"
    else:
        date, src = "0000-00-00 00:00", "none"
    if inline and max(inline) > date[:10]:
        date, src = max(inline) + " 00:00", "explicit"
    return date, src


def date_files(root: Path, today: str):
    repo = repo_root(root)
    touched = last_touch(repo, root) if repo else {}
    return [(*file_date(p, repo, touched, today), p) for p in discover(root)]


def blame(path: Path):
    """[(line_no, date, hash, subject, text)] for a tracked file, else None."""
    repo = repo_root(path.parent)
    if not repo:
        return None
    out = git(repo, "blame", "--line-porcelain", "--", str(path.resolve()))
    if not out:
        return None
    rows, cur, subjects = [], {}, {}
    for line in out.splitlines():
        if re.match(r"^[0-9a-f]{40} \d+ \d+", line):
            parts = line.split()
            cur = {"hash": parts[0], "line": int(parts[2])}
        elif line.startswith("author-time "):
            cur["date"] = utc(dt.datetime.fromtimestamp(int(line.split()[1]), dt.timezone.utc))
        elif line.startswith("summary "):
            subjects[cur["hash"]] = line[8:]
        elif line.startswith("\t"):
            h = cur["hash"]
            uncommitted = set(h) == {"0"}
            rows.append((cur["line"], "uncommitted" if uncommitted else cur["date"],
                         h, "" if uncommitted else subjects.get(h, ""), line[1:]))
    return rows


def show(root: Path, p: Path) -> str:
    try:
        return p.relative_to(root).as_posix()
    except ValueError:
        return p.as_posix()


def lines_mode(root: Path, files):
    for f in files:
        p = (root / f) if (root / f).exists() else f
        rows = blame(p.resolve())
        if rows is None:
            print(f"{p}: not tracked by git", file=sys.stderr)
            continue
        print(f"\n== {show(root, p.resolve())}")
        groups = []
        for n, date, h, subj, text in rows:
            if groups and groups[-1][2] == h and groups[-1][1] == n - 1:
                groups[-1][1] = n
            else:
                groups.append([n, n, h, date, subj, text])
        for start, end, h, date, subj, text in groups:
            span = f"L{start}" if start == end else f"L{start}-{end}"
            print(f"  {span:<11} {date:<16} {h[:7]}  [{subj[:50]}]  {text.strip()[:60]}")


def keep(p: Path, paths, exclude) -> bool:
    s = p.as_posix()
    norm = lambda xs: [x.replace("\\", "/") for x in xs]
    return (not paths or any(x in s for x in norm(paths))) and not any(x in s for x in norm(exclude))


def term_mode(root: Path, extras, terms, today: str, paths, exclude, since: str, width: int):
    pats = [re.compile(re.escape(t), re.I) for t in terms]
    hits = []
    for base in [root, *extras]:
        repo = repo_root(base)
        touched = last_touch(repo, base) if repo else {}
        for p in discover(base):
            if not keep(p, paths, exclude):
                continue
            text = p.read_text(encoding="utf-8", errors="replace")
            if not any(pt.search(text) for pt in pats):
                continue
            rows = blame(p) if repo else None
            if rows is None:  # untracked: every line takes the file's date
                date, src = file_date(p, repo, touched, today)
                rows = [(i, date, "", src, t) for i, t in enumerate(text.splitlines(), 1)]
            for n, date, h, subj, line in rows:
                if date >= since and any(pt.search(line) for pt in pats):
                    hits.append((date, show(root, p), n, h[:7], subj, line.strip()))
    hits.sort(key=lambda r: (r[0], r[1], r[2]))
    print(f"Lines mentioning {terms}, oldest first. Later lines override earlier ones.\n")
    for date, path, n, h, subj, line in hits:
        print(f"{date}  {path}:{n}  {h or '-'}  [{subj[:60]}]\n    {line[:width] if width else line}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("story_root", type=Path)
    ap.add_argument("--extra", type=Path, action="append", default=[],
                    help="Another folder of dated sources (e.g. the auto-memory folder). Repeatable.")
    ap.add_argument("--paths", nargs="+", default=[],
                    help="Keep only files whose path contains one of these substrings.")
    ap.add_argument("--exclude", nargs="+", default=[],
                    help="Drop files whose path contains one of these substrings (e.g. chapters/ drafts/).")
    ap.add_argument("--term", nargs="+", default=[], help="Timeline of lines mentioning these terms.")
    ap.add_argument("--since", default="", help="--term: only lines dated on or after YYYY-MM-DD.")
    ap.add_argument("--width", type=int, default=0,
                    help="--term: cut each line to this many characters (default 0: whole line).")
    ap.add_argument("--lines", nargs="+", type=Path, default=[],
                    help="Line-by-line dates for these files (relative to story_root, or to the current folder).")
    a = ap.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    root = a.story_root.resolve()
    if not root.is_dir():
        print(f"not a directory: {root}", file=sys.stderr)
        return 2
    today = dt.date.today().isoformat()
    extras = []
    for e in a.extra:
        if e.is_dir():
            extras.append(e.resolve())
        else:
            print(f"skipping --extra (not a directory): {e}", file=sys.stderr)

    if a.lines:
        lines_mode(root, a.lines)
        return 0
    if a.term:
        term_mode(root, extras, a.term, today, a.paths, a.exclude, a.since, a.width)
        return 0

    rows = date_files(root, today)
    for e in extras:
        rows += date_files(e, today)
    rows = [r for r in rows if keep(r[2], a.paths, a.exclude)]
    rows.sort(key=lambda r: (r[0], r[2].as_posix()))
    print("Oldest first. Later rows override earlier ones where they disagree.\n")
    for date, src, p in rows:
        print(f"{date}  {src:<9} {show(root, p)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
