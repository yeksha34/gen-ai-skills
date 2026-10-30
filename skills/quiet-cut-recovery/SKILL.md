---
name: quiet-cut-recovery
description: Recover text that a work's revisions quietly cut or softened — specific detail, vivid imagery, strong wording, distinctive voice, dialogue lines, named things, whole passages — when no later decision negated it. Recovered text is made consistent with the work as it stands now: its characters, places, rules, terms and timeline. Uses git history and the recency-precedence stack to separate quiet loss from deliberate cuts, lists the candidates, and restores the ones the user picks with their original strength intact. Use whenever the user says text was watered down, toned down, flattened, genericised, lost, dropped or "quietly removed" in a revision; asks to restore, recover or put back material from earlier versions; or wants to audit revisions for lost detail, even if they don't say "recovery". Also use after a big rewrite, translation, polish or alignment pass on any long-running text kept in git.
---

# Quiet-cut recovery

Revisions of long-running text tend to leak strength. A rewrite keeps the beat but swaps a concrete image for an abstraction. An overhaul drops the odd detail that made a scene feel real. A polish pass trims a sharp line of dialogue, a precise number, a named object, a character's verbal tic. Nobody decided any of this: no instruction asked for it, and nothing in the work's rules forbids it. The text just got blander, one sentence at a time. The stance this skill holds: revisions never weaken or drop material unless a decision says so. This skill finds what slipped through and puts it back.

What counts as lost is whatever the user cares about, judged by what a piece of text *is*, not by whether it matches a word list. Typical losses:
- concrete, sensory or specific detail replaced by something vaguer;
- strong or distinctive wording replaced by milder, safer or more generic wording;
- a character's voice flattened (tics, dialect, register, idiom);
- dialogue lines, asides or reactions removed;
- named people, places, objects, numbers or dates dropped;
- whole passages or files removed without a stated reason.

**Depends on `recency-precedence`.** Load it first. A cut is deliberate only when something on the decision stack negates the content. Everything else that lost material is a quiet cut.

## Workflow

### 1. Scope
Agree on the project root and, if the user gave one, a range: files, folders, dates or commits. Ask what kind of loss matters most if it isn't clear. With no range, cover the whole history. On a long history, start with the summary and then go commit by commit.

### 2. Find what left the files
Use the bundled script (`scripts/removed_spans.py`, standard library only). It walks `git log -p --word-diff`, so it catches single words dropped from sentences that otherwise survived.

```bash
# Where the cuts cluster: counts per commit and tag
python <skill>/scripts/removed_spans.py <root> --summary --exclude translations

# The hits for one commit or range, with surrounding text
python <skill>/scripts/removed_spans.py <root> --commit <hash> --tags CUT SOFTENED
python <skill>/scripts/removed_spans.py <root> --since 2026-01-01 --paths drafts/ --exclude translations

# Every removal, watched terms or not, for a close look at one commit
python <skill>/scripts/removed_spans.py <root> --commit <hash> --all
```

**Exclude files that keep old wording on purpose**, for example a translation file or an archive that holds the original lines. They would otherwise make weakened text look as if it "survives". `--exclude` drops a file from both the hits and the survival search.

**Watched terms.** `references/watch_terms.txt` holds regexes for the words that matter in this project: invented terms, character names, key objects, signature phrases, the register the user wants kept. It only filters and ranks. While it has no active patterns, the script shows every removal, as with `--all`. Add terms when the history is long and you need to narrow it. Keep using `--all` when you suspect losses the list can't see, such as a vivid image made of ordinary words.

**Tags** (pointers for judgement, not verdicts):

| Tag | Meaning |
|---|---|
| `CUT` | Words removed and nothing put in their place. |
| `SOFTENED` | Replaced by text without the removed watched terms. |
| `FILE-GONE` | The whole file was deleted. |
| `TRANSLATED` | Replaced by text in Devanagari script: a language edit, never a cut, so it's hidden unless you pass `--all`. |
| `MOVED` | The removed words reappear elsewhere on the same line. Hidden unless you pass `--all`. |
| `REWORDED` | The replacement kept the same watched terms. Hidden unless you pass `--all`. |

With no watched terms, every replacement reads as `REWORDED`, so judge `SOFTENED` yourself from the before and after text.

**Markers:**
- `still-there` means the removed words still sit in the current file between the same neighbouring words, so the cut was later undone.
- `survives:` means the removed text (5 or more words) exists in another current file.
- `[subject names a removal]` flags commit subjects such as "remove…", "drop…" or "revert…".

The script prints times in UTC, the same as `recency_order.py`. A bare `--since` date means 00:00 that day.

### 3. Sort each hit against the stack
For each removed bit, ask in this order.

1. **Was it a correction, not a cut?** Some edits are corrections. Never roll them back to the older version:
   - **Language moves.** A passage moved into another language the work uses, or into a translation file or footnote. The language edit is the newer decision on the stack and stands as written.
   - **Trait fixes.** A word changed to fit the character or thing it describes: their name or title, kind, anatomy, speech, role. Check the character's or entity's card before calling a swap a softening.
   - **Factual fixes.** A wrong date, number, name or rule corrected to match the rest of the work.
2. **Was it negated?** A cut is deliberate when another decision on the stack negates *that content*:
   - a commit subject or body that names removing this kind of thing ("remove the flashback…" covers the flashback, not an unrelated line of dialogue). Read the body with `git log -1 --format=%B <hash>`: it often says a passage was moved or why something went;
   - a revert of specific additions;
   - a ruling in memory, lore, rules or a style guide that bans or replaces it;
   - a dropped file, chapter or draft whose events were replaced by different ones.

   A rename negates only the term, not the content around it: retiring an old name doesn't retire the detail in that sentence. Generic subjects like "refine", "polish", "update", "align", "overhaul", "rewrite", "pass", "enrich" or "follow the drafts" are not decisions to remove content. Treat their losses as quiet.
3. **Does it survive?** It may still be there: a `still-there` or `survives:` hit, or the same detail re-added later or moved elsewhere in the file (look at the current text at the anchor). It may also have been rephrased just as strongly.
4. **Did the beat survive?** Count a rewrite when the same beat is still in the text but its specific or distinctive detail is gone. Skip passages rewritten into different events. The detail belonged to events that no longer happen.
5. **Does it fit the work as it stands now?** Test the removed bit against the top of the stack, not against the version it was first written in:
   - **Who:** every character in it still exists, is present in this scene, and acts as their card says now (traits, speech, name, pronouns).
   - **Where:** the place and its features match the current setting.
   - **What:** rules and lore allow it, including who knows what and how they learned it.
   - **When:** it agrees with what has and hasn't happened by this point.

   If it fits, it's a candidate. If a mismatch can be fixed while the detail stays at full strength, it's still a candidate: note the fix for step 5. If the detail itself depends on something the work no longer allows (a character who is no longer there, a rule that now forbids it, an event that no longer happens), the work has negated it, and it stays cut.
6. **Is it inside the project's rules?** Anything the project's rules, style guide or the user's standing instructions ban stays out whatever the history says. Hold back borderline lines and name them for the user to decide.

Whatever is left after these six questions is a **quiet cut**: a candidate for recovery.

### 4. List the candidates
Show the user a numbered list grouped by file. Keep each entry short:

```
drafts/<file>.md
  Q1  <date> <hash> "<commit subject>" · SOFTENED
      removed: "…the removed text in full…"   (was: "…words before ‹removed› words after…")
      now:     "…what the line says today…"
      goes back at: drafts/<file>.md:<line>
      adapt: <terms and fixes needed, or none>
      as restored: "…the bit exactly as it would go in, adapted…"
```

- **removed:** the removed text in full, with enough surrounding words to place it.
- **goes back at:** the current `file:line` where it would go, found by locating the surviving context.
- **adapt:** the term swaps and fixes from step 3, or "none".
- **as restored:** the exact text that would go in, so the user judges the version that fits the work now, not the old one.

Name protected or finished files (published chapters, released docs) in the list too, but mark them "(protected: only if you name it)". Then stop and let the user pick: all, some numbers, or all except some.

### 5. Restore the picks
- **Put it back where the beat now is.** Anchor on the surviving context. If the passage has moved or been reworded since, place the bit where that beat now sits.
- **Make it fit the work, and change nothing else.**
  - Swap negated terms for the current ones: current names, titles and invented words, and the project's own spelling and style conventions.
  - Apply the fixes from step 3: the right character, pronoun, place detail or knowledge channel.
  - If the surrounding line is now in another language, the recovered bit goes in that language too, following the project's rules for it.
  - Beyond that, keep the original words. **Keep its strength intact:** no milder synonym, no shortening, no paraphrase into vagueness.
- **Never drop or rewrite surrounding lines** to make room. Restoring only adds. The only exceptions are the fixes above and the minimal joining a sentence needs to read.
- **No version talk** in the text. The restored text reads as if it had always been there.
- **Protected files only when named.** Restore into a protected file only when the user names that file. A broad "restore all" doesn't count as naming one.

### 6. Check
- Run `git diff` on each touched file. Every change should be an insertion, a term swap or a fix. Nothing existing should be removed or weakened.
- Read each restored passage against the work once more: its characters, places, rules and timeline as they stand now.
- Re-run the script on the same range. The recovered hits should now be `survives:`, where the text is long enough to match.
- Report what was restored (`file:line`), what was skipped as deliberate (one line each, naming the negating decision), and anything you weren't sure about.
