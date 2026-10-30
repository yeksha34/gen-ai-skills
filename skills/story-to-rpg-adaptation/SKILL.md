---
name: "story-to-rpg-adaptation"
description: "Adapt a story into an RPG design scoped to its format: quest progression, side quests, branching plotlines, NPCs, compact node dialog, barks and inner-voice lines."
---

# Story → RPG Adaptation

Adapt a story into an RPG design document: quest progression, branching plotlines, side quests, NPCs and dialog that fit the game's format and scope.

**This is an adaptation, not a transformation.** A transformation carries the whole story over beat by beat. An adaptation keeps what the story *is* — its central conflict, key turning points, the main characters' arcs, its tone and the few moments people remember — and rebuilds those for a game, under the game's limits. Most RPGs, and short ones especially, cannot hold a one-to-one version of a story. Cutting, merging and compressing are the core of the job, done on purpose, and every major cut is written down so the user can see it and reverse it.

A story is a sequence of things that *happen to* characters. An RPG is a sequence of things the *player does*, in a world they move through at their own pace. In an RPG, dialog interrupts play: it sets up and pays off what the player does, and the player decides when to start it, what to ask and when to leave.

## Step 1 — Intake

Ask only for what is missing, in one short question (multiple choice where possible), then proceed.

1. **The story.** Pasted text, an attached file, or a known work named by title. For a published work, work from its plot. Write new dialog; don't reproduce its text beyond a short iconic phrase.
2. **The mode.**
   - **Mode 1, play as a character.** One story character is the player character (PC) and everyone else is an NPC. Suggest the protagonist by default.
   - **Mode 2A, outsider allied with the hero.** Every story character is an NPC. The PC is a new person in the story's world who helps the main character.
   - **Mode 2B, outsider allied with the villain.** Same as 2A, but the PC serves the antagonist.
   - **Mode 2, open allegiance.** The PC starts as an outsider and chooses a side at a hinge point, so 2A and 2B become branches of one game.
3. **The RPG format and scope.** The subtype (action RPG, narrative RPG or CRPG, JRPG, mobile RPG, tabletop) and roughly how long a playthrough lasts. This decides how much of the story survives, so it matters more than any other setting. If you can't ask, assume a **short narrative RPG of 1–2 hours** and say so at the top of the document.
4. **Optional settings.** Ending policy (canon, divergent or mixed), how much branching, and an export format (JSON, Ink, Yarn). Defaults are a canon spine with divergent optional endings, branch-and-bottleneck structure, and markdown only.

## Step 2 — Set the scope budget

Choose a tier, write its budget into the document, and treat it as a hard limit. When the story offers more than the budget allows, cut more; don't grow the game.

| Tier | Playtime | Main quests (stages each) | Side quests | Speaking NPCs | Hinge points | Endings |
|---|---|---|---|---|---|---|
| Micro (game jam, prototype) | 10–30 min | 1 (3–4) | 0–1 | 2–4 | 0–1 | 1–2 |
| Short | 1–3 h | 2–4 (3–5) | 2–4 total | 4–8 | 1–2 | 2–3 |
| Mid | 5–15 h | 5–10 (4–6) | 6–15 total | 8–20 | 2–4 | 3–4 |
| Large | 20 h+ | 10+, grouped into parts | 15+ | 20+ | 4–6 | 3–5 |

Main quests are the progression points. In a story longer than a single arc, cut at turning points, so each main quest ends like a chapter: a goal reached, a revelation, or a reversal. A story with more arcs than the budget allows gets its arcs merged, not more quests.

## Step 3 — Analyze, then decide what to adapt

**Break the story down** (it goes in the document, compactly):
- **Cast:** each character's role, goal and arc.
- **Places**, and the **key objects**.
- **Beats:** the plot in order, each tagged as *turning point*, *action*, *revelation* or *transition*.
- **Interiority:** passages where the story narrates a character's thoughts, doubts, memories or motives. This is raw material for inner-voice lines (Step 9).
- **Core:** the central conflict and theme in one line each, plus the 3–5 moments a fan would be upset to lose.

**Then sort every beat, character, place and subplot into one of these:**
- **Keep.** Core turning points, the climax, iconic moments, and the PC's (or hero's, or villain's) arc.
- **Compress.** A run of events becomes one playable sequence. Travel and time skips become a map move or a single line.
- **Merge.** Minor characters with similar functions become one NPC. Several locations become one hub. Several obstacles become one encounter.
- **Convert.** Exposition and backstory move into the world: item descriptions, letters, murals, overheard lines, memory thoughts, or one optional conversation.
- **Spin off.** An off-page event, a gap in the story or a minor subplot becomes a side quest, but only if the budget has room.
- **Cut.** Anything that doesn't serve the core and doesn't fit the budget.
- **Invent, sparingly.** Add connective tissue only where the game needs it: a reason for the PC to be somewhere, or a player objective where the story had none. Keep every invention consistent with the story's tone and logic, and label it as new.

Record these calls in an **Adaptation Notes** table: element, decision, reason. This is how the user steers the adaptation, so keep it honest. Don't quietly drop things.

## Step 4 — Apply the mode

### Mode 1: the player is a story character
- The PC's actions in the story become objectives, phrased as player actions ("Escape the burning village", not "Ram escapes").
- At the PC's real decision points, offer a choice. The canon option is one of them, marked `(canon)`, alongside 1–2 plausible alternatives (see Step 5 for which ones branch).
- The PC's spoken lines become dialog options in a few tones that suit the character. A darker option can appear as a temptation, but keep it true to the character.
- Events the PC didn't witness can't be played directly. Turn them into reports, rumors or letters, or cut them.

### Mode 2A: outsider helping the hero
- Give the PC a role with a reason to be present (messenger, mercenary, healer, guide, servant, merchant), a default name, and a note that it's customizable.
- Canon events still happen, and the PC makes them possible. For each kept beat, ask *what had to be true for this to work?* That condition becomes the PC's objective.
- The hero keeps their defining moments. The PC clears the path to the duel; the hero fights it.
- The hero acts as a quest giver and a trust track. Failing a support quest makes the hero's beat cost something.

### Mode 2B: outsider helping the villain
- Give the PC an understandable motive: debt, loyalty, ideology, ambition, coercion, or a grudge against the hero.
- Quests are the villain's plans made concrete: gather, recruit, deceive, sabotage, intercept.
- State the ending policy up front. **Canon holds:** the villain falls, and the PC's arc is about their final choice. **Divergent:** the villain can win, with at least one mixed ending.
- Give the villain a motive and a line they won't cross (or the clear absence of one). Include at least one moment where the PC can push back, defect or double down.

## Step 5 — Derive choice-based plotlines

Branches come from the story itself, not from arbitrary options.

1. **Find hinge points.** A hinge is a moment where a character could believably have chosen otherwise, given their motives, and where that choice would change what follows. Most decisions in a story are not hinges. Rank the candidates by how believable the alternative is and how much it changes, and keep as many as the budget allows.
2. **Follow the consequences.** For each alternative, work out what changes, who reacts and how, and where the story goes next. The alternate path must obey the story's own logic and characters. A branch that breaks them is fanfic, which is fine if the user wants it, but label it.
3. **Choose a structure that fits the scope:**
   - **Branch and bottleneck** (default): paths split and rejoin at major story beats, and flags remember the difference. This is the cheapest structure.
   - **Foldback:** short detours that return to the main path with changed details.
   - **Delayed consequences:** a choice in an early quest pays off in a later one. This gives the most felt agency for the least writing; use it generously.
   - **Faction or allegiance split:** after one major hinge, the quest line splits for good. This is the natural fit for Mode 2 open allegiance. It is expensive, so give it at most one per game below the Large tier.
   - **Avoid** fully independent branching (every choice splits): 3 choices with 2 options each already make 8 paths.
4. **Separate flavor from branch.** Most choices only *flavor* a scene: they change a reaction, a line, a disposition or a flag. Only hinge points *branch* it, changing the path. In Micro and Short tiers, nearly everything is flavor.
5. **Give every branch its own payoff.** Each one needs its own climax beat and an ending, or at least a distinct epilogue. A branch that fizzles out feels like a punishment.

Document the hinges in a **Branch Map**: hinge, canon option, alternatives, consequence chain, where each path rejoins or ends.

## Step 6 — Side quests (only within budget)

Draw side quests from the story's gaps, minor characters, places mentioned once and backstory, not from generic templates. Each side quest must do at least one of these:
- deepen a main character,
- pay off later in the main line (an item, an ally, information or an alternate solution to a quest),
- reveal lore that matters.

Drop any side quest that does none of these. If the budget allows 0–1 side quests, pick the single strongest one, or none. Side quests may unlock inside a window and expire when the story moves on; say so.

## Step 7 — NPCs

Write a sheet for each speaking NPC within the budget. Composites list which story characters they absorb. In Mode 2, story characters keep their canon personalities; state their attitude toward the PC.

- **Micro and Short:** one block per NPC: name, role, what they want from the PC, voice (2–3 traits plus one sample line).
- **Mid and Large:** add locations by quest, disposition and what changes it, what they know or can give, quests they give or appear in, and how they react on each branch.

Voice is the part that matters most. Take it from the story: vocabulary, formality, verbal tics. Compact dialog only works when each NPC sounds distinct within one line.

## Step 8 — Dialog, compacted for RPG play

Players skim, and every line costs writing, translation, voice acting and UI space. Write the fewest lines that deliver the beat, the character's voice and the choice. Prefer subtext over explanation, and let the world carry exposition. Write only conversations that do a job: start a quest, present a key choice, deliver a revelation, or close a quest. Cut greetings, recaps and filler, and summarize fetch steps in one line.

### Line budgets by RPG format

| Format | NPC line length | Lines per exchange | Options per choice | Notes |
|---|---|---|---|---|
| Action RPG | ≤ 15 words | 1–3 | 2 | Short and skippable; heavy use of barks |
| Mobile RPG | ≤ 15 words | 1–3 | 2 | Speech bubbles |
| Short narrative RPG | ≤ 25 words | 2–5 | 2–3 | Hub dialog with ask-about topics |
| CRPG / JRPG | ≤ 40 words | 3–8 | 3–4 | Skill or stat checks, reputation, companion interjections |
| Tabletop | Read-aloud ≤ 4 sentences | N/A | N/A | Read-aloud box plus GM notes |

If an exchange runs over budget, cut lines before cutting meaning. Merge two NPC lines, turn a question-and-answer into a single statement, or move the information into an item.

### RPG-specific dialog structure
- **Hubs.** Long conversations are a hub of topics the player can pick in any order and return to. Required information must not sit behind an optional topic.
- **State-dependent lines.** An NPC says something different before a quest, during it, after it, and on each branch. Write at least the before and after lines for quest givers.
- **Repeat lines.** Talking to an NPC again gives one short line, not the whole conversation.
- **Quest-log consistency.** Each dialog node that changes the quest state names the log update, so the dialog and the journal agree.
- **Barks.** Ambient and triggered one-liners: a list per trigger (`ON_SPOT: "There!" / "Over here!"`, `ON_ENTER_TOWN`, `AFTER_MQ2`). Barks are cheap reactivity; use them to show that the world noticed a choice.
- **Tabletop.** Use a read-aloud box plus bullet notes (what the NPC wants, knows, and will say if pushed) instead of trees.

### Notation

```
MQ1-D1  VASHA: The river took the bridge. Nothing's crossed since.
  > I'll go.            → D2  {+accepted_mq1} [log: MQ1 started]
  > What's it pay?      → D3  {vasha -1}
  > [Insight 2] You're hiding something.  → D4
  > Later.              → END
  ( thought ) She keeps glancing at the far bank.
```

- The node ID starts with the quest ID. The speaker is in caps.
- `>` marks a player option and `→` points to the next node or `END`.
- `{}` holds effects: `+flag` sets a flag, `npc ±n` changes disposition. `[log: …]` is a quest-log update.
- A `[Skill n]` prefix marks a check. `(canon)` marks the canon option in Mode 1.
- `( thought )` marks an inner-voice line (Step 9).
- Player option text is a short paraphrase (≤ 8 words). Write the full spoken line only if the game voices the PC.
- Every branch must resolve. Every flag that is set must be read somewhere; otherwise delete it.

## Step 9 — Inner voice (the PC talking to themselves)

Stories narrate interiority that games usually lose. Bring the best of it back as inner-voice lines. To derive one, take a passage of narrated thought ("He feared the old man was lying"), turn it into a compressed first-person present line ("He's lying. Or he's afraid."), and attach it to a trigger.

**Types, from cheapest to richest:**
1. **Reaction thoughts.** One line when something happens, or when the player examines an object.
2. **Hint thoughts.** "The well. I should look there." They steer the player without a quest marker. Use them sparingly, and never just to repeat the objective.
3. **Memory thoughts.** Short flashes of the past, which are a good home for backstory the adaptation would otherwise cut.
4. **Choice-framing thoughts.** The inner conflict, stated in a line or two just before a hinge, so the stakes are felt.
5. **Inner voices as speakers.** The self split into named voices that argue (DUTY vs. DESIRE, FEAR vs. PRIDE), each lining up with a choice option. They can be tied to stats or skills, in the style of Disco Elysium. Use this for stories built on inner struggle, and only in narrative RPGs and CRPGs.

**Sourcing by mode.**
- **Mode 1:** take the thoughts from the character's canon interiority and keep them true to how that character thinks.
- **Mode 2:** the outsider has no canon inner life, so every thought is invented. Use them as the player's outside view of the hero or villain. In 2B, the inner voice is where the moral pressure lives: doubts, rationalizations, the pull to defect.

**RPG limits.** Inner-voice lines are one-liners (≤ 15 words), tied to triggers, and they never block play. Don't narrate what the player can already see, and don't tell the player how to feel about a choice they haven't made. A thought should add something the screen can't show: motive, memory, doubt or subtext.

## Step 10 — Assemble the document

Use this structure, and omit sections that don't apply.

```markdown
# <Story> — RPG Adaptation (<Mode>)
Source · Mode · Player character · Format & tier (with budget) · Ending policy · Branch structure

## 1. Story Core
Central conflict · theme · must-keep moments (3–5)
## 2. Adaptation Notes
| Element | Decision (keep / compress / merge / convert / spin off / cut / invented) | Reason |
## 3. Branch Map
| Hinge | Canon | Alternatives | Consequences | Rejoins at / ends in |
## 4. Quest Map
| ID | Type | Title | Story source | Unlocks when | Leads to |
(mermaid flowchart of quests and branches for Mid and Large tiers)
## 5. Main Quests
### MQ1 — <Title>
Summary · Giver · Unlocks when
Stages: player objectives, each with location and completion condition
Choices: situation → options → consequence (flavor or branch)
Rewards · Flags set
Dialog: compact nodes, before/after lines, inner-voice lines
## 6. Side Quests
Same fields, plus "Source in story" and "Payoff"
## 7. NPCs
## 8. Barks
## 9. Endings
Conditions → outcome → one epilogue line per key NPC
## 10. Flag Index   (Mid and Large tiers, or whenever there are more than ~6 flags)
```

**Export (on request).** JSON with `meta`, `npcs[]`, `quests[]` (id, type, giver, requires, stages, rewards, sets_flags, dialog_start), `dialog{node_id: {speaker, line, options[{text, next, requires, effects, canon}]}}`, `barks{trigger: [lines]}` and `endings[]`. Ink or Yarn scripts can be produced too. Check that every `next` points to an existing node or `END`, and every required flag is set somewhere.

For Mid and Large tiers, build in stages. Send the Story Core, Adaptation Notes, Branch Map and Quest Map first, so the user can redirect before the detailed quests and dialog are written.

## Delivery

Deliver a document the user can keep and edit: a doc artifact by default, or the format they ask for (.md, .docx, JSON, Ink, Yarn). Close with one line on what was produced and one natural next step, such as "restore any cut element?", "add another hinge?" or "export to Yarn?".

## Checks before delivering

- **Budget.** Quest, NPC, hinge and ending counts are within the tier, and dialog lines are within the format's budget. Spot-check the longest ones.
- **Fidelity.** All the must-keep moments are present and the central conflict reads clearly. Every cut, merge and invention appears in the Adaptation Notes.
- **Branches.** Every hinge comes from the story's logic, every branch has a payoff, and the canon path is playable when the ending policy calls for it.
- **Agency.** Every objective is a player action, and choices sit at meaningful moments.
- **Mode.** Mode 1 offers choices at the PC's decision points. Mode 2 never takes the hero's or villain's defining moment.
- **Integrity.** Every branch resolves, every flag is used, quest-log updates match the dialog, and progression gates run in a valid order.