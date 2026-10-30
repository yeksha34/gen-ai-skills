---
name: recency-precedence
description: Read a long-running story's reference material (lore, plot, rules, character cards, settings, scene lists, decision notes, memory) as a stack of decisions applied oldest to newest. Each newer bit adds to, refines or negates the older ones, so newer decisions replace legacy text instead of being contradicted by it. Use before writing, revising, planning, summarising or checking anything that leans on reference files in a story that is still evolving, where plot and lore files hold legacy text that later discussion, drafts or memory have overtaken. Also use when the user says a draft used an old name, meaning or rule; when two reference files disagree; or when the user asks what is current or canon now. Use it even if the user doesn't mention legacy text or recency.
---

# Recency precedence

An unfinished story's reference files are written once and then drift. Decisions keep being made in conversation, and they land wherever the work happened to be: a redefinition in one lore file, a rename in a candidates list, a new usage in a fresh draft, a ruling in memory. The older files are rarely brought up to date. Reading `plot/` or `lore/` as written gives you the world as it was, not as it is now, and prose built on it contradicts what the user already decided.

The rule this skill applies:

> **Decisions stack. Apply them in time order, oldest first. Each newer one either adds to, refines or negates what came before. The current state is what remains at the top of the stack.**

- **Add:** a newer bit sets down something not decided before. It stacks on top, and everything below stays in force.
- **Refine:** a newer bit sharpens an older one. The older bit stands, with the newer detail on top.
- **Negate:** a newer bit contradicts, retires, renames or redefines an older one. The newer bit replaces it.

The comparison is always relative, between two bits. When they conflict, the newer one wins, whether or not it is the newest thing in the story. A decision that nothing later touches **stays valid however old it is**. Age alone never makes text stale. Only a newer bit that says otherwise does.

This holds across layers. A newer draft, card or decision note that negates an older lore entry overrides it. A legacy line does not win just because it sits in a folder called "lore" or "rules". The only thing newer than every file is the current conversation.

**A negated bit needs no change.** It stays as written in its old file, and the stack resolves it every time the material is read. So the skill works at **read time only**. It never rewrites, annotates, flags or "fixes" older files. The story is still being written, so treat nothing here as a fixed map. Discover the sources and their dates fresh on every run.

## Workflow

### 1. Name what the task touches
List the entities and terms the task depends on: characters, kinds or species, places, rules, titles, invented words, relations, timeline facts. Gather only these, the way you would gather lore for a scene. Pulling everything in invites legacy text in with it.

For each entity, collect **every name it has gone by**: old and new names, translations, other scripts (Devanagari and roman), singular and plural forms. A rename leaves no trace under the new name in old files, and no trace under the old name in new ones. You need both to see the handover.

### 2. Find the sources and their order
Use the bundled script (`scripts/recency_order.py`, standard library only, runs from any folder). Point it at the story root and add the project's auto-memory folder with `--extra`. That folder is named in your system prompt and holds dated rulings that often never reached the repo.

```bash
# Which files exist, oldest first (narrow with --paths substrings)
python <skill>/scripts/recency_order.py <story_root> --extra <memory_dir> --paths lore rules plot characters

# Timeline of every line that mentions the terms, each dated by its own last change
python <skill>/scripts/recency_order.py <story_root> --extra <memory_dir> --term "old name" "new name" "नया नाम"

# One file broken into line ranges by the commit that last changed them
# (path relative to the story root, or to the current folder)
python <skill>/scripts/recency_order.py <story_root> --lines <file>
```

A term timeline on a busy story is mostly prose hits. Start narrow, then widen:
- `--exclude chapters/ drafts/ translations` keeps the reference layers.
- `--since YYYY-MM-DD` drops the long legacy tail once you know where the change happened.
- `--paths` keeps only matching paths.
- `--width N` shortens lines. By default lines print whole, so you can read the full claim.

Drop the excludes again when you need step 3's evidence from dependent content.

**Prefer `--term` and `--lines`.** File-level dates are coarse: one sweeping commit can touch a whole folder and make every file look equally new. Line-level dates show which sentence is old inside a recently touched file, and each line carries its commit subject.

How dates are taken, strongest first:
- git commit time for tracked text;
- a `modified:` stamp in frontmatter (memory files);
- a later ISO date written in the text ("on 2026-10-28 …");
- file mtime only as a last resort, because it moves whenever a file is re-saved.

### 3. Stack the decisions, oldest first
Walk the timeline in order and apply each bit to the stack for its entity.
- **Additions and refinements pile up.** The current state of an entity is usually several bits from different times taken together, not one line.
- **A newer bit negates an older one when it:**
  - **retires** it explicitly ("retired", "deprecated", "does not exist", "not canon", "replaced by", "renamed to", a struck or retired candidate);
  - **redefines** it: same term, different meaning or rule;
  - **renames** it: a new name adopted for the same entity;
  - **does it differently in newly written content**: a draft, scene list or card written later that consistently treats the entity another way. Dependent content counts as evidence. If the user's later drafts all do X, X is current even though the older card says Y.
- **A negation removes only the bit it contradicts.** The rest of the older file's decisions on that entity stay on the stack.

Keep the stack as a private working note: entity → the bits still standing (source, date), plus the bits negated and what negated them. Don't write it to a file, and don't show it unless the user asks.

### 4. Weigh the edge cases
- **Explicit beats incidental at a similar time.** A line can carry a recent date only because a sweep touched it: a rename pass, a spelling pass, a translation pass (look at the commit subject). That line may still say the old thing. A deliberate redefinition from around the same time outranks it. Only text actually written anew in a later commit can overturn a decision.
- **Overrides get overridden.** A memory note or decisions file is not final. It is one dated source, and a later file can retire what it proposed. Keep reading to the end of the timeline before settling.
- **Proposals stay proposals until adopted.** Candidate lists, "maybe", "options" and "not canon yet" don't replace anything on their own. A later source can adopt them one by one (a card switches to the new name) or wholesale ("drafts take every name from the candidates list"). A wholesale adoption makes the whole list current within the scope it names: for new drafts, every candidate counts even if no draft uses it yet. Files outside that scope keep the old form until they are adopted too. A list's own "not canon" header is negated by the later adoption.
- **Kept on purpose is not current.** When a newer source says old wording stays somewhere by the user's choice (for example, old terms left in finished prose), that wording is valid in that place. It is not evidence about what is current anywhere else, and it is not a contradiction to fix.
- **Predecessor material sorts first.** Files from an earlier version of the project (old names, old taxonomy, long untouched) are the oldest layer. They supply nothing that a later source contradicts.
- **The conversation is newest.** Anything the user said in this session overrides every file.

### 5. Ask only about real ties
Ask the user only when two claims conflict and neither is clearly newer, for example both from the same commit or day with no explicit retirement. Also ask when the newest claim is genuinely ambiguous. Otherwise resolve by recency without comment. Don't re-open decisions the timeline has already settled, and don't ask the user to confirm something a newer source already says.

### 6. Write from the top of the stack
- Produce the task's output from what is still standing on the stack. Never let a negated name, meaning or rule leak back in because it was in the file you happened to read last.
- The stack is reference, not prose. The usual leak rules apply: lore shapes the writing and is never restated in it (see the `story-direction` skill if it is loaded).
- **Leave older files as they are.** Negated bits need no change, so don't list them as out of date, don't offer to update them, and don't edit them. Edit an older file only when the user asks for that file to change.

## Examples (shapes, not facts)

**Redefinition across layers.** An older rules file defines a term one way. A lore file redefines it a few days later, with a commit subject about that change. A memory note records the same redefinition. Drafts written after that use the new sense. Top of the stack: the new sense. The rules line is negated and stays as written. The rest of that rules file still stands. If the task is to write a scene, write it with the new sense.

**An override that was overturned.** A memory note proposes a new word for a kind of being. A day later, a candidates file marks that word as retired, a lore file adopts a different word, and cards switch to it. Top of the stack: the adopted word. The memory note's proposal is negated even though memory feels authoritative, because it is older than the retirement. Its other rulings, which nothing later touched, still stand.

**A sweep that didn't change the meaning.** A setting file's line about a term is dated yesterday, but the commit subject says "translation pass", and the sentence still carries the old meaning. A deliberate redefinition from the day before outranks it. The current meaning comes from the redefinition.

**A real tie.** Two files changed in the same commit give a character different ranks, and nothing else mentions the rank. Ask the user which is current.
