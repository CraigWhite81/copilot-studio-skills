# ROCKET Framework — Full Reference

## Framework Overview

ROCKET is a structured framework for writing high-quality Microsoft Copilot Studio agent instructions.

| Letter | Dimension | Core Question |
|--------|-----------|---------------|
| R | Role | Who is the agent? |
| O | Objectives | What must the agent achieve? |
| C | Constraints | What must the agent never do? |
| K | Knowledge | What data grounds the agent? |
| E | Execute | What does the agent need to do? |
| T | Tone | How should the agent sound? |

---

## Scoring Reference

### Score 1 — Lacking
Absent, critically vague, or actively harmful to agent behaviour.

### Score 2 — Partial
Addressed but lacks specificity, has significant gaps, or relies on the agent inferring too much.

### Score 3 — Complete
Fully defined, specific, and actionable. Another person could reproduce the intent without clarification.

---

## Dimension Details

### R — Role
✅ Named persona aligned to use case, explicitly states what the agent represents
❌ "You are a helpful assistant" with no context, no name, role contradicts use case

### O — Objectives
✅ 2–5 outcome-focused objectives framing the *why*, optionally ranked
❌ Task lists masquerading as objectives, too many to prioritise, none stated

### C — Constraints
✅ Explicit topic exclusions, defined handoff triggers, behaviour for unknown topics
❌ "Use common sense", constraints buried in other sections, none defined

### K — Knowledge
✅ Named sources with clear intent, refresh cadence noted, fallback behaviour defined
❌ Sources listed with no purpose, no fallback (hallucination risk), none defined

### E — Execute
✅ Each capability has a trigger condition, sequencing defined, failure handling per outcome
❌ "Use x tool when relevant", tools listed without trigger logic, no failure handling

### T — Tone
✅ Specific style guidance, language variants, handling for emotional or frustrated users
❌ "Be professional and helpful", tone inconsistent with role, none defined

---

## Score Interpretation

| Range | Label | Recommendation |
|-------|-------|----------------|
| 0–5 | Houston, we have a problem | Do not deploy. Fundamental rework needed. |
| 6–9 | Rocket grounded | Still in development. Address lacking dimensions first. |
| 10–14 | On the launchpad | Close to ready. Focus on partial dimensions. |
| 15–18 | Rocket has liftoff | Production ready. Schedule periodic review. |

---

## Example: Well-Scored Instructions (16/18)