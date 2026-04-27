---
name: skill-evaluator
description: Use this skill to create evals (test suites) for Claude Code / OpenClaw skills. Produces eval.yaml files with test cases and graders, and guides the RED-GREEN-REFACTOR testing cycle to bulletproof a skill against rationalization.
---

# Skill Evaluator

## Purpose

Create structured, runnable evals for skills.

An eval proves a skill works under pressure — not just in ideal conditions. Combine the OpenAI evals format (data schema + graders) with TDD pressure scenarios (from superpowers/meta/writing-skills).

## When To Use

- "создай тесты для скилла X"
- "напиши eval для learning-ai-product"
- "как проверить что скилл работает"
- "скилл не работает, как отладить"
- After writing a new skill before deploying it
- When a skill was violated and you want to prevent future violations

## Two Levels of Evals

### Level 1 — Output structure tests

Verify the skill produces the right format, sections, language, and constraints.
Fast, cheap, deterministic. Run on every change.

### Level 2 — Pressure / compliance tests

Verify the skill holds under pressure — time pressure, sunk cost, authority, urgency.
Slow, expensive, probabilistic. Run before deploying a skill.

## Eval File Format

Each skill gets one `eval.yaml` file at `evals/<group>/<skill-name>.yaml`.

```yaml
name: <skill-name>
skill_id: <group/category/name>
description: <what this eval tests>
model: ollama/kimi-k2.6:cloud # model under test

# Schema of test case inputs
data_source:
  type: custom
  item_schema:
    type: object
    properties:
      user_message:
        type: string
        description: The user message sent to the skill
    required: [user_message]

# Graders — conditions that must ALL pass for a test to pass
graders:
  # Contains: output must include a string
  - name: <grader-name>
    type: contains
    input: "{{ output }}"
    value: "<expected substring>"

  # Not contains: output must NOT include a string
  - name: <grader-name>
    type: not_contains
    input: "{{ output }}"
    value: "<forbidden substring>"

  # Regex: output must match a pattern
  - name: <grader-name>
    type: regex
    input: "{{ output }}"
    pattern: "<regex>"

  # LLM judge: a secondary LLM evaluates the output against a criterion
  - name: <grader-name>
    type: llm_judge
    input: "{{ output }}"
    criteria: "<one-sentence description of what PASS means>"
    # Pass = judge returns YES or PASS; Fail = NO or FAIL

# Test cases
test_cases:
  - id: <kebab-case-id>
    description: <what this test checks>
    user_message: "<the user input>"
    graders: [<grader-name>, ...] # which graders apply to this case
    # omit graders to run all

  # Pressure scenario test (Level 2)
  - id: pressure-<scenario>
    type: pressure
    description: <what pressure is being applied>
    user_message: |
      IMPORTANT: This is a real scenario. You must choose and act.

      <scenario description with 3+ combined pressures>

      Options:
      A) <correct option>
      B) <shortcut option>
      C) <rationalization option>

      Choose A, B, or C.
    expected_choice: A
    graders: [chose-correct-option]
```

## Grader Design Rules

### Contains graders

- Target section headers, key phrases, required output elements
- Use exact strings from the skill's output format spec
- One grader per distinct required element

### LLM judge graders

Write criteria as: **"The output [does/does not] [specific observable thing]"**

Good:
```
The response is primarily written in Russian
The response contains a scored table of AI tool ideas
The response does NOT contain any executable code
The response clearly separates what the user must build vs what AI can help with
```

Bad:
```
The response is good
The response follows the skill
The output is correct
```

### Pressure scenario graders

```yaml
- name: chose-correct-option
  type: llm_judge
  input: "{{ output }}"
  criteria: "The response chooses option A or explicitly follows the skill's required behavior, not options B or C"
```

## Workflow

### Step 1 — Map the skill's output contract

Read the skill's `## Output Format` section. Every required section, phrase, and constraint becomes a grader.

### Step 2 — Write happy path test cases

3–5 representative inputs covering:
- Minimal valid input
- Typical usage
- Edge case (too broad, too narrow, missing data)

### Step 3 — Write pressure scenarios (for compliance skills)

For skills that enforce discipline (block shortcuts, require steps, have Hard Gates):
- Identify what the skill PREVENTS the AI from doing
- Write a scenario where doing the wrong thing is tempting
- Combine 3+ pressures: time + sunk cost + authority + urgency

### Step 4 — RED phase

Run evals WITHOUT loading the skill (bare model, no system prompt from skill).
Document which graders fail and which rationalizations appear.

### Step 5 — GREEN phase

Run evals WITH the skill loaded.
All graders should pass.

### Step 6 — REFACTOR

For each new rationalization the model finds:
- Add a `not_contains` or `llm_judge` grader that catches it
- Re-run until all graders pass

## Output Format

When the user asks to create evals for a skill, produce:

```md
## Eval Plan: [skill-name]

### Output contract (what the skill guarantees)
- [list of observable guarantees]

### Graders
[table: name | type | what it checks]

### Test cases
[table: id | input summary | pressures if any | expected outcome]

### YAML
[complete eval.yaml ready to save]
```

## Style Rules

- Write in English (eval files are code, not prose).
- Be concrete: graders check exact strings, not vibes.
- Prefer `contains` over `llm_judge` when possible — cheaper and deterministic.
- Every compliance skill needs at least one pressure scenario.
- The eval should be runnable: no TODOs, no placeholder values.
