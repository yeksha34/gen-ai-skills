#!/usr/bin/env python3
"""List text that left a project's files, commit by commit, oldest first.

Usage:
  python removed_spans.py <root> --summary --tags CUT SOFTENED FILE-GONE
  python removed_spans.py <root> --paths drafts/ lore/ --exclude translations --since 2026-10-20
  python removed_spans.py <root> --commit c89d342 --all
  python removed_spans.py <root> --lexicon my_terms.txt --context 120

Walks `git log -p --word-diff` over <root>, so a single word dropped from a
sentence that otherwise survived shows up, not only whole deleted lines. Each change
(a run of removed and/or added words between unchanged text) is kept when its removed
side matches the watched terms (references/watch_terms.txt by default), unless
--all is given or the term file has no active patterns. Files matched by --exclude
are skipped everywhere, including the "survives" search, so exclude files that keep
old wording on purpose.

Tags:
  CUT         words removed, nothing put in their place
  SOFTENED    replaced by text that lacks the removed watched terms
  FILE-GONE   the whole file was deleted in this commit
  TRANSLATED  replacement is in Devanagari: a move into another language,
              which is a language edit, never a cut (only with --all)
  MOVED       the removed text reappears elsewhere on the same line (only with --all)
  REWORDED    replacement keeps the same watched terms (only with --all)
Markers:
  still-there        the removed words still sit in the current file between the same
                     neighbouring words (the cut was later undone)
  survives: <files>  the removed text (5+ words) exists in another current file
  [subject names a removal]  the commit subject says remove/drop/revert/...
All of these are pointers for judgement, never verdicts.

Times print in UTC to the minute, the same as recency_order.py.
"""
import argparse
import datetime as dt
import re
import subprocess
import sys
from pathlib import Path

DEFAULT_LEXICON = Path(__file__).resolve().parent.parent / "references" / "watch_terms.txt"
REMOVAL_WORDS = re.compile(r"\b(remov|drop|cut|revert|undo|retir|renam|delet|strip|trim|clean)", re.I)
DEV = "ऀ-ॿ"
DEVANAGARI = re.compile(f"[{DEV}]")
HUNK = re.compile(r"^@@ -(\d+)(?:,\d+)? \+(\d+)(?:,\d+)? @@")
TAGS = ["CUT", "SOFTENED", "TRANSLATED", "FILE-GONE", "MOVED", "REWORDED"]


def git(repo: Path, *args: str) -> str:
    r = subprocess.run(["git", "-C", str(repo), *args], capture_output=True,
                       text=True, encoding="utf-8", errors="replace")
    return r.stdout if r.returncode == 0 else ""


def utc(iso: str) -> str:
    return dt.datetime.fromisoformat(iso).astimezone(dt.timezone.utc).strftime("%Y-%m-%d %H:%M")


def load_lexicon(path: Path) -> list[re.Pattern]:
    """Regex per line. `= a|b` is whole Devanagari words, `~ a|b` Devanagari word starts."""
    pats = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line[0] == "=":
            line = f"(?<![{DEV}])(?:{line[1:].strip()})(?![{DEV}])"
        elif line[0] == "~":
            line = f"(?<![{DEV}])(?:{line[1:].strip()})"
        pats.append(re.compile(line, re.I))
    return pats


def watched(text: str, lex) -> set[str]:
    return {m.group(0).lower() for p in lex for m in p.finditer(text)}


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip().lower()


def parse_log(out: str):
    """[(hash, stamp, subject, file, status, changes)].

    A change is a dict: line (old-side line number), before / after (old-side text
    around it), rem, add."""
    records, commit, rec, cur = [], None, None, None
    old_line, before, pending = 0, "", []

    def old_side(text: str):
        nonlocal before, pending
        before = (before + text)[-400:]
        for c in pending:
            c["after"] += text
        pending = [c for c in pending if len(c["after"]) < 300]

    def close():
        nonlocal cur
        if cur and rec is not None and (cur["rem"].strip() or cur["add"].strip()):
            rec[5].append(cur)
            pending.append(cur)
        cur = None

    for line in out.splitlines():
        if line.startswith("@@C "):
            close()
            h, d, s = line[4:].split("\t", 2)
            commit, rec = (h, utc(d), s), None
        elif line.startswith("diff --git "):
            close()
            rec, before, pending = [*commit, "", "", []], "", []
            records.append(rec)
        elif rec is not None and line.startswith("--- "):
            if line[4:] != "/dev/null":
                rec[3] = line[6:] if line[4:6] == "a/" else line[4:]
        elif rec is not None and line.startswith("+++ "):
            if line[4:] == "/dev/null":
                rec[4] = "FILE-GONE"
            else:
                rec[3] = line[6:] if line[4:6] == "b/" else line[4:]
        elif rec is not None and HUNK.match(line):
            close()
            old_line, before, pending = int(HUNK.match(line).group(1)), "", []
        elif rec is not None and line[:1] in (" ", "-", "+", "~"):
            tag, text = line[0], line[1:]
            if tag == " ":
                close()
                old_side(text)
            elif tag == "~":
                if cur:
                    cur["rem" if cur["rem"] and not cur["add"] else "add"] += " "
                old_side(" ")
                old_line += 1
            else:
                if not cur:
                    cur = {"line": old_line, "before": before, "rem": "", "add": "", "after": ""}
                cur["rem" if tag == "-" else "add"] += text
                if tag == "-":
                    old_side(text)
                    cur["before"] = cur["before"]  # before stays as it was at the change start
    close()
    return [tuple(r) for r in records if r[3]]


def classify(c, lex, same_line_adds: str):
    rem, add = c["rem"], c["add"]
    rt, at = watched(rem, lex), watched(add, lex)
    if norm(rem) and norm(rem) in norm(same_line_adds):
        return "MOVED", rt
    if DEVANAGARI.search(add):  # moved into (or between) Hindi and Sanskrut: a language edit
        return "TRANSLATED", rt
    if not add.strip():
        return "CUT", rt
    if rt - at:
        return "SOFTENED", rt - at
    return "REWORDED", rt


def still_there(c, current: str) -> bool:
    """Removed words still in the current file between the same neighbouring words."""
    left = " ".join(norm(c["before"]).split()[-3:])
    right = " ".join(norm(c["after"]).split()[:3])
    probe = norm(f"{left} {c['rem']} {right}")
    return len(probe) > len(norm(c["rem"])) and probe in current


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("root", type=Path)
    ap.add_argument("--paths", nargs="+", default=[], help="Keep only files whose path contains one of these.")
    ap.add_argument("--exclude", nargs="+", default=[],
                    help="Skip files whose path contains one of these, in hits and in the survives search.")
    ap.add_argument("--since", default="", help="Only commits on or after this date (YYYY-MM-DD means 00:00).")
    ap.add_argument("--until", default="", help="Only commits on or before this date (YYYY-MM-DD means 23:59).")
    ap.add_argument("--commit", nargs="+", default=[], help="Only these commits (hash prefixes).")
    ap.add_argument("--lexicon", type=Path, default=DEFAULT_LEXICON)
    ap.add_argument("--all", action="store_true", help="Every removal, watched terms or not, MOVED and REWORDED too.")
    ap.add_argument("--context", type=int, default=80, help="Characters of surrounding text shown each side.")
    ap.add_argument("--tags", nargs="+", default=[], help=f"Only these tags ({' '.join(TAGS)}).")
    ap.add_argument("--summary", action="store_true", help="Counts per commit and tag instead of the hits.")
    a = ap.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    root = a.root.resolve()
    top = git(root, "rev-parse", "--show-toplevel").strip()
    if not top:
        print(f"not in a git repository: {root}", file=sys.stderr)
        return 2
    repo = Path(top)
    rel = root.relative_to(repo.resolve()).as_posix() or "."
    lex = load_lexicon(a.lexicon)
    if not lex:  # no watched terms yet: show every removal
        a.all = True
    wants = lambda f: (not a.paths or any(p in f for p in a.paths)) and not any(x in f for x in a.exclude)

    args = ["log", "--reverse", "-M", "-p", "--word-diff=porcelain", "--unified=1",
            "--format=@@C %H\t%aI\t%s"]
    if a.since:
        args.append(f"--since={a.since} 00:00" if len(a.since) == 10 else f"--since={a.since}")
    if a.until:
        args.append(f"--until={a.until} 23:59" if len(a.until) == 10 else f"--until={a.until}")
    out = git(repo, *args, "--", rel)

    corpus = {}
    for p in root.rglob("*"):
        if p.is_file() and p.suffix.lower() in {".md", ".txt", ".markdown"}:
            f = p.relative_to(root).as_posix()
            if not any(x in f for x in a.exclude):
                corpus[f] = norm(p.read_text(encoding="utf-8", errors="replace"))
    prefix = "" if rel == "." else rel + "/"

    last_commit, shown, summary = None, 0, {}
    for h, stamp, subj, file, status, changes in parse_log(out):
        if a.commit and not any(h.startswith(c) for c in a.commit):
            continue
        short = file[len(prefix):] if file.startswith(prefix) else file
        if not wants(short):
            continue
        hits = []
        if status == "FILE-GONE":
            removed = "".join(c["rem"] for c in changes)
            terms = watched(removed, lex)
            if terms or a.all:
                hits.append(("FILE-GONE", {"line": 1, "before": "", "rem": f"({len(removed.split())} words)",
                                           "add": "", "after": ""}, terms, ""))
        else:
            adds_by_line = {}
            for c in changes:
                adds_by_line[c["line"]] = adds_by_line.get(c["line"], "") + " " + c["add"]
            for c in changes:
                if not c["rem"].strip():
                    continue
                tag, terms = classify(c, lex, adds_by_line.get(c["line"], ""))
                if not a.all and (not watched(c["rem"], lex) or tag in ("MOVED", "REWORDED", "TRANSLATED")):
                    continue
                mark = ""
                if still_there(c, corpus.get(short, "")):
                    mark = "  still-there"
                elif len(norm(c["rem"]).split()) >= 5:
                    where = [f for f, t in corpus.items() if norm(c["rem"])[:120] in t]
                    if where:
                        mark = f"  survives: {', '.join(where[:3])}"
                hits.append((tag, c, terms, mark))
        if a.tags:
            hits = [x for x in hits if x[0] in a.tags]
        if not hits:
            continue
        if a.summary:
            row = summary.setdefault(h, {"stamp": stamp, "subj": subj, "files": set()})
            row["files"].add(short)
            for x in hits:
                key = x[0] + ("*" if x[3] else "")
                row[key] = row.get(key, 0) + 1
                shown += 1
            continue
        if last_commit != h:
            flag = "  [subject names a removal]" if REMOVAL_WORDS.search(subj) else ""
            print(f"\n=== {stamp} {h[:7]}  {subj}{flag}")
            last_commit = h
        for tag, c, terms, mark in hits:
            shown += 1
            print(f"  {short} ~L{c['line']}  {tag}  terms: {', '.join(sorted(terms)) or '-'}{mark}")
            if c["before"].strip():
                print(f"    before:  …{' '.join(c['before'].split())[-a.context:]}")
            print(f"    removed: {' '.join(c['rem'].split())}")
            if tag not in ("CUT", "FILE-GONE"):
                print(f"    added:   {' '.join(c['add'].split())}")
            if c["after"].strip():
                print(f"    after:   {' '.join(c['after'].split())[:a.context]}…")
    if a.summary:
        cols = ["CUT", "SOFTENED", "FILE-GONE"] + (["TRANSLATED", "MOVED", "REWORDED"] if a.all else [])
        print("Counts per tag; '+n' is how many of them are marked still-there or survives.\n")
        print("stamp (UTC)       commit   " + " ".join(f"{t[:9]:>10}" for t in cols) + "  files  subject")
        for h, r in summary.items():
            flag = " [names a removal]" if REMOVAL_WORDS.search(r["subj"]) else ""
            cells = []
            for t in cols:
                n, s = r.get(t, 0) + r.get(t + "*", 0), r.get(t + "*", 0)
                cells.append(f"{n}+{s}" if s else str(n))
            print(f"{r['stamp']}  {h[:7]}  " + " ".join(f"{x:>10}" for x in cells)
                  + f"  {len(r['files']):>5}  {r['subj'][:70]}{flag}")
    print(f"\n{shown} hit(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
