# Copilot Studio ROCKET Skill

A Claude Code skill for scoring Microsoft Copilot Studio agent instructions 
using the ROCKET framework.

## ROCKET Framework

| Letter | Dimension | Question |
|--------|-----------|----------|
| R | Role | Who is the agent? |
| O | Objectives | What must it achieve? |
| C | Constraints | What must it never do? |
| K | Knowledge | What grounds the agent? |
| E | Execute | What does it need to do? |
| T | Tone | How should it sound? |

Each dimension scores 1–3. Total: 18 points.

## Installation

### Global install — works across all your projects
```bash
mkdir -p ~/.claude/skills
git clone https://github.com/YOUR-USERNAME/copilot-studio-rocket-skill.git ~/.claude/skills/copilot-studio-rocket
```

### Project-level install — just for one project
```bash
git clone https://github.com/YOUR-USERNAME/copilot-studio-rocket-skill.git .claude/skills/copilot-studio-rocket
```

## Usage

Once installed, just talk to Claude naturally:

- "Score my agent using the ROCKET framework" and paste your instructions
- "ROCKET score this agent" with a .yaml file referenced
- "Review these Copilot Studio instructions with ROCKET"

## Scoring

| Score | Label |
|-------|-------|
| 0–5 | Houston, we have a problem |
| 6–9 | Rocket grounded — still in dev |
| 10–14 | On the launchpad — almost there |
| 15–18 | Rocket has liftoff — production ready |

## Credits

ROCKET framework created by Craig White. 
Designed for Microsoft Copilot Studio agent governance.