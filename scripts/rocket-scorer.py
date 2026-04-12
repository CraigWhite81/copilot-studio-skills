#!/usr/bin/env python3
"""
ROCKET Framework - Copilot Studio YAML Instruction Extractor
Extracts agent instructions from a Copilot Studio YAML file and prints them
ready for scoring by the ROCKET skill.

Usage:
    python3 scripts/rocket_scorer.py path/to/agent.yaml
"""

import sys

def extract_yaml_simple(content):
    target_keys = [
        "instructions",
        "systemPrompt",
        "system_prompt",
        "agentInstructions",
        "prompt",
        "description",
    ]
    
    lines = content.splitlines()
    results = {}
    current_key = None
    current_value_lines = []
    in_multiline = False

    for line in lines:
        stripped = line.strip()
        
        for key in target_keys:
            if stripped.startswith(f"{key}:"):
                if current_key and current_value_lines:
                    results[current_key] = "\n".join(current_value_lines).strip()
                current_key = key
                current_value_lines = []
                remainder = stripped[len(key)+1:].strip()
                if remainder and remainder != "|" and remainder != ">":
                    current_value_lines.append(remainder)
                    current_key = None
                    results[key] = remainder
                else:
                    in_multiline = True
                break
        else:
            if in_multiline and current_key:
                if line.startswith("  ") or line.startswith("\t"):
                    current_value_lines.append(line.strip())
                else:
                    results[current_key] = "\n".join(current_value_lines).strip()
                    current_key = None
                    in_multiline = False

    if current_key and current_value_lines:
        results[current_key] = "\n".join(current_value_lines).strip()

    return results


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/rocket_scorer.py <path_to_agent.yaml>")
        print("\nThis tool extracts agent instructions from a Copilot Studio YAML file.")
        print("Pass the output to Claude with the ROCKET skill active for scoring.")
        sys.exit(1)

    filepath = sys.argv[1]

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File not found: {filepath}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    print(f"\n{'='*60}")
    print(f"ROCKET Framework - Agent Instruction Extractor")
    print(f"File: {filepath}")
    print(f"{'='*60}\n")

    extracted = extract_yaml_simple(content)

    if extracted:
        print("Extracted instruction fields:\n")
        for key, value in extracted.items():
            print(f"--- {key} ---")
            print(value)
            print()
    else:
        print("No standard instruction fields found automatically.")
        print("The full file content is shown below for manual review:\n")
        print(content)

    print(f"\n{'='*60}")
    print("Paste the above into Claude with the ROCKET skill active.")
    print("Or just say: 'ROCKET score this agent' and share the file.")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()