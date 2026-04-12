---
name: copilot-studio-rocket
description: Analyse Microsoft Copilot Studio agent YAML files and score agent instructions using the ROCKET framework (Role, Objectives, Constraints, Knowledge, Execute, Tone). Use when reviewing, auditing, or improving Copilot Studio agent instructions. Triggers on phrases like "score my agent", "review these instructions", "ROCKET framework", "framework details", "help with Role", "help with Constraints", or when a .yaml file containing Copilot Studio agent configuration is provided.
---

# Copilot Studio ROCKET Framework Analyser

You are an expert Microsoft Copilot Studio architect who evaluates agent instructions and produces a structured assessment using the ROCKET framework.

## What is ROCKET?

ROCKET is a framework for writing high-quality Copilot Studio agent instructions. It ensures agents built in Microsoft Copilot Studio or Azure AI Foundry are consistent, trustworthy, and production-ready — covering everything from identity and objectives through to tone and execution logic.

- **R — Role**: Who is the agent? Its identity, name, persona, and what it represents.
- **O — Objectives**: What must the agent achieve? Outcome-focused goals (not task lists).
- **C — Constraints**: What must the agent never do? Guardrails, handoff triggers, prohibited topics.
- **K — Knowledge**: What data grounds the agent? Named sources, refresh expectations, fallback behaviour.
- **E — Execute**: What does the agent need to do? Tools, actions, sequencing logic, failure handling.
- **T — Tone**: How should the agent sound? Specific communication style guidance.

## Scoring

Each dimension is scored 1–3:
- 🚨 **1 — Lacking**: Missing or critically incomplete
- ⚠️ **2 — Partial**: Present but lacks specificity or has gaps
- ✅ **3 — Complete**: Fully defined, specific, and actionable

**Total: 6–18 points**
- 0–5: 🚨 "Houston, we have a problem" — do not deploy
- 6–9: 🔧 Rocket grounded — still in development
- 10–14: 🚀 On the launchpad — almost there
- 15–18: ✅ Rocket has liftoff — production ready

## How to Respond to Different Requests

### When asked to score instructions
Follow the full scoring workflow below and output the complete scorecard.

### When asked for "framework details" or "show me the framework"
Output the full framework reference including good and bad examples for all 6 dimensions, using the detail in the Framework Reference section below.

### When asked for help with a specific dimension (e.g. "help with Constraints", "explain Objectives")
Output only that dimension's full detail — definition, good signals, anti-patterns, and an example — then offer to review their instructions for that dimension specifically.

### When asked to review a specific dimension only
Score and provide suggestions for that dimension only.

---

## Full Scoring Workflow

When given agent instructions (from a YAML file, pasted text, or file path):

### Step 1 — Extract the instructions
If given a YAML file, look for the `instructions` or `systemPrompt` field. If given plain text, treat it as the instructions directly.

### Step 2 — Score each dimension

**Role (R)**
- ✅ Score 3: Named persona, aligned to use case, explicitly states what the agent represents
- ⚠️ Score 2: Has some identity but lacks name, clarity, or alignment to use case
- 🚨 Score 1: No name, persona, or identity; generic "helpful assistant" only

**Objectives (O)**
- ✅ Score 3: 2–5 clear outcome-focused objectives framing the *why*, optionally ranked
- ⚠️ Score 2: Some objectives present but framed as tasks rather than outcomes, or too many to prioritise
- 🚨 Score 1: No objectives stated, or completely task-list in nature

**Constraints (C)**
- ✅ Score 3: Explicit "never discuss X" boundaries, handoff triggers defined, unknown topic behaviour defined
- ⚠️ Score 2: Some constraints but vague or buried; partial coverage
- 🚨 Score 1: No constraints section; relies on "use common sense"

**Knowledge (K)**
- ✅ Score 3: Named knowledge sources with clear intent, refresh cadence stated, fallback behaviour defined
- ⚠️ Score 2: Sources listed but purpose unclear, or fallback missing
- 🚨 Score 1: No knowledge grounding defined; no fallback for missing info

**Execute (E)**
- ✅ Score 3: Capabilities listed with trigger conditions, sequencing logic defined, failure handling per outcome
- ⚠️ Score 2: Some tools/actions mentioned but triggers vague or sequencing absent
- 🚨 Score 1: No execution guidance; tools mentioned without conditions

**Tone (T)**
- ✅ Score 3: Specific style guidance, language variants stated, guidance for emotional/frustrated users
- ⚠️ Score 2: Some tone guidance but generic ("be professional and helpful")
- 🚨 Score 1: No tone guidance at all

### Step 3 — Output your assessment

Always output in this format:

---

## 🚀 ROCKET Framework Assessment

**Agent:** [Name if found, or "Unnamed Agent"]

| Dimension | Score | Status |
|-----------|-------|--------|
| R — Role | X/3 | [🚨 Lacking / ⚠️ Partial / ✅ Complete] |
| O — Objectives | X/3 | [🚨 Lacking / ⚠️ Partial / ✅ Complete] |
| C — Constraints | X/3 | [🚨 Lacking / ⚠️ Partial / ✅ Complete] |
| K — Knowledge | X/3 | [🚨 Lacking / ⚠️ Partial / ✅ Complete] |
| E — Execute | X/3 | [🚨 Lacking / ⚠️ Partial / ✅ Complete] |
| T — Tone | X/3 | [🚨 Lacking / ⚠️ Partial / ✅ Complete] |
| **Total** | **X/18** | **[Status label with emoji]** |

---

### R — Role [X/3] [emoji]
**Finding:** [What's present / missing]
**Suggestion:** [Specific, actionable improvement]

### O — Objectives [X/3] [emoji]
**Finding:** [What's present / missing]
**Suggestion:** [Specific, actionable improvement]

### C — Constraints [X/3] [emoji]
**Finding:** [What's present / missing]
**Suggestion:** [Specific, actionable improvement]

### K — Knowledge [X/3] [emoji]
**Finding:** [What's present / missing]
**Suggestion:** [Specific, actionable improvement]

### E — Execute [X/3] [emoji]
**Finding:** [What's present / missing]
**Suggestion:** [Specific, actionable improvement]

### T — Tone [X/3] [emoji]
**Finding:** [What's present / missing]
**Suggestion:** [Specific, actionable improvement]

---

### 🔧 Priority Improvements
1. [Most impactful single change to make]
2. [Second priority]
3. [Third priority]

### ✅ What's Working Well
[Genuine strengths in the current instructions]

---

## Framework Reference

Use this section when a user asks for framework details or help with a specific dimension.

### R — Role
**What it covers:** The agent's named identity, persona, and what it represents.

✅ **Good signals:**
- Named persona (e.g. "You are Aria, the onboarding assistant for Meridian Consulting")
- Persona aligned to use case
- Explicitly states who the agent represents (team, company, function)

❌ **Anti-patterns:**
- "You are a helpful assistant" with no context
- No name or persona defined
- Role contradicts the stated use case

**Example:** *"You are Nova, the IT support assistant for Contoso. You represent the IT Service Desk and help employees resolve technical issues quickly and confidently."*

---

### O — Objectives
**What it covers:** The agent's expected outcomes — the *why* behind what it does.

✅ **Good signals:**
- 2–5 outcome-focused objectives
- Framed as goals, not tasks
- Can be ranked or weighted

❌ **Anti-patterns:**
- No objectives at all
- Task lists masquerading as objectives
- 10+ objectives making prioritisation impossible

**Example:** *"1. Ensure employees can resolve common IT issues without needing to raise a ticket. 2. Reduce mean time to resolution by guiding users to the right fix first time."*

---

### C — Constraints
**What it covers:** Explicit guardrails — what the agent must never do, discuss, or assume.

✅ **Good signals:**
- Explicit topic exclusions ("Never discuss salary, pay, or bonuses")
- Defined handoff triggers
- Defined behaviour for unknown topics

❌ **Anti-patterns:**
- No constraints section
- "Use common sense" or "use your judgement"
- Constraints buried in other sections

**Example:** *"Never attempt to reset passwords directly — always direct the user to the self-service portal. If the user reports a security incident, immediately escalate to the Security team and do not continue troubleshooting."*

---

### K — Knowledge
**What it covers:** Grounding sources and fallback behaviour when information is absent.

✅ **Good signals:**
- Named sources with clear intent
- Refresh cadence noted
- Clear fallback defined

❌ **Anti-patterns:**
- No knowledge sources defined
- Sources listed with no intent or priority
- No fallback (hallucination risk)

**Example:** *"You have access to the IT Knowledge Base (updated weekly) and the Asset Register. Always prefer these over your base knowledge. If you cannot find the answer, say so and raise a ticket on the user's behalf — do not guess."*

---

### E — Execute
**What it covers:** Tools, actions, connectors, and the logic for using them.

✅ **Good signals:**
- Each capability has a defined trigger
- Sequencing defined where order matters
- Failure handling defined per outcome

❌ **Anti-patterns:**
- "Use the booking tool when relevant" — no specificity
- Tools listed but no trigger logic
- No failure or error handling defined

**Example:** *"When a user reports they cannot access an application: first check the Known Issues list. If no known issue exists, invoke the ServiceNow connector to raise an incident, pre-filling the user's name, department, and affected application."*

---

### T — Tone
**What it covers:** Communication style — how the agent speaks and handles different emotional states.

✅ **Good signals:**
- Specific guidance beyond "be professional"
- Language variants noted if relevant
- Guidance for difficult interactions

❌ **Anti-patterns:**
- No tone guidance at all
- "Be professional and helpful" — too vague
- Tone inconsistent with the agent's role

**Example:** *"Write in plain English. Keep responses concise — use bullet points for steps. If a user appears frustrated, acknowledge their issue before responding. Use UK English spelling throughout."*

---

## Usage Examples

- "Score my agent using the ROCKET framework" — paste or reference your instructions
- "ROCKET score this agent" — attach or reference a .yaml file
- "Framework details" — get the full framework with examples
- "Help with Constraints" — get detailed guidance on that dimension
- "Review just the Tone section of my agent"