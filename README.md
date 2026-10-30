# GenAI Agentic Skills

A collection of agentic skills for GenAI agents and assistants. Each skill is maintained on its own dedicated branch.

## Skills

| Skill | Branch | Description |
| :--- | :--- | :--- |
| **gangadhar-shuddh-hindi** | [`gangadhar-shuddh-hindi`](https://github.com/yeksha34/gen-ai-skills/tree/gangadhar-shuddh-hindi) | Speak or write in ultra-shuddh, Sanskritised Hindi in the voice of Gangadhar (from Shaktimaan). |
| **log-bug** | [`log-bug`](https://github.com/yeksha34/gen-ai-skills/tree/log-bug) | Log, triage, fix-track, and close bugs or tech-debt items. |
| **native-html-first** | [`native-html-first`](https://github.com/yeksha34/gen-ai-skills/tree/native-html-first) | Check for built-in HTML elements or attributes before writing JavaScript, custom components, or libraries. |
| **native-pronunciation-spelling** | [`native-pronunciation-spelling`](https://github.com/yeksha34/gen-ai-skills/tree/native-pronunciation-spelling) | Spell Indic words in English or Devanagari text as actually pronounced natively. |
| **quiet-cut-recovery** | [`quiet-cut-recovery`](https://github.com/yeksha34/gen-ai-skills/tree/quiet-cut-recovery) | Recover specific detail, vivid imagery, or distinctive voice quietly cut or softened across revisions. |
| **recency-precedence** | [`recency-precedence`](https://github.com/yeksha34/gen-ai-skills/tree/recency-precedence) | Resolve conflicting story reference files by treating decisions as an oldest-to-newest precedence stack. |
| **record-decision** | [`record-decision`](https://github.com/yeksha34/gen-ai-skills/tree/record-decision) | Write and track Architecture Decision Records (ADRs). |
| **release-tag** | [`release-tag`](https://github.com/yeksha34/gen-ai-skills/tree/release-tag) | Cut tagged release branches with synchronized documentation and status. |
| **rules-check-manual** | [`rules-check-manual`](https://github.com/yeksha34/gen-ai-skills/tree/rules-check-manual) | Validate and check drafts against agent rules using the agent itself as judge. |
| **story-direction** | [`story-direction`](https://github.com/yeksha34/gen-ai-skills/tree/story-direction) | Direct and maintain long-form stories across lore, scenes, drafts, and chapters. |
| **story-host** | [`story-host`](https://github.com/yeksha34/gen-ai-skills/tree/story-host) | Act as game master / host engine with turn context, narration, and secret keeping. |
| **story-to-rpg-adaptation** | [`story-to-rpg-adaptation`](https://github.com/yeksha34/gen-ai-skills/tree/story-to-rpg-adaptation) | Adapt a story into an RPG design (quest progression, side quests, branching plotlines, NPCs, dialog). |
| **story-to-vn-adaptation** | [`story-to-vn-adaptation`](https://github.com/yeksha34/gen-ai-skills/tree/story-to-vn-adaptation) | Adapt narrative prose into visual novel scripts, routes, and asset budgets. |
| **structured-prompts** | [`structured-prompts`](https://github.com/yeksha34/gen-ai-skills/tree/structured-prompts) | Design and refactor system prompts and agent instructions with XML tag discipline. |
| **track-feature** | [`track-feature`](https://github.com/yeksha34/gen-ai-skills/tree/track-feature) | Track and manage feature lifecycles and synchronize requirement specs. |
| **world-builder** | [`world-builder`](https://github.com/yeksha34/gen-ai-skills/tree/world-builder) | Build and extend world lore, characters, settings, arcs, and rules. |
| **world-lint** | [`world-lint`](https://github.com/yeksha34/gen-ai-skills/tree/world-lint) | Lint, validate, and navigate world lore cross-references and card webs. |

---

## How to Fetch and Merge a Subtree

To import and keep a skill branch synchronized with another project repository using Git subtree:

### 1. Add and Fetch the Remote

In your target project repository, add this repo as a remote and fetch:

```bash
git remote add gen-ai-skills https://github.com/yeksha34/gen-ai-skills.git
git fetch gen-ai-skills
```

### 2. Add a Skill Subtree

Add the desired skill branch (e.g. `log-bug`) to your project under your desired directory prefix (e.g. `.agents/skills` or `skills`):

```bash
git subtree add --prefix=skills gen-ai-skills log-bug --squash
```

### 3. Fetch and Merge Updates

To fetch and merge the latest updates from a skill branch:

#### Option A: Using `git subtree pull`
```bash
git subtree pull --prefix=skills gen-ai-skills log-bug --squash
```

#### Option B: Using `git fetch` and `git merge -s subtree`
```bash
git fetch gen-ai-skills <branch-name>
git merge -s subtree -Xsubtree=<prefix> gen-ai-skills/<branch-name>
```
