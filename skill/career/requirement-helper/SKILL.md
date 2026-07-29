---
name: requirement-helper
description: Guide software requirements through a mandatory read-only advisory stage and an explicitly authorized delivery stage. Use when the user submits a feature request, product change, bug fix, PRD, enhancement, or implementation task; asks whether a requirement is worth doing, how to implement or split it, what they can learn from it, or how to turn it into credible resume or interview evidence; wants step-by-step coding guidance or direct implementation; or asks to review a solution, patch, diff, or PR. Normalize the requirement, inspect project context, evaluate value and risk, recommend the next action, route to Manual or Automatic delivery, and verify outcomes.
---

# Requirement Helper

Turn a software requirement into a deliberate, learning-oriented delivery process. Always understand and evaluate the requirement before implementation. Respond in Chinese unless the user asks otherwise.

## Use A Layered Workflow

Keep three dimensions separate:

- **Stage**: Advisory → Delivery → Verification.
- **Delivery strategy**: None, Manual, or Automatic.
- **Depth**: Light, Standard, or Deep.

Do not treat analysis-only, plan-only, Manual, Automatic, and Review as equivalent modes. Analysis and planning describe scope, Manual and Automatic describe who writes the code, and Review describes the request type.

## Enforce Authorization Boundaries

- Keep Advisory, planning, diagnosis, and Review read-only.
- Enter Automatic delivery only after the user explicitly authorizes code changes for the current requirement. Authorization from an unrelated or materially different task does not carry over.
- Let an explicit no-change instruction override implementation language.
- Read and obey repository instructions such as `AGENTS.md` before giving project-specific advice or making changes.
- Treat authorization to edit code as separate from authorization to stage, commit, push, deploy, change production data, or perform other external writes. Never infer those permissions.
- Preserve user changes and stay within the agreed scope.
- Follow user and repository verification constraints. If adding tests is forbidden or inappropriate, use existing tests, compilation, static checks, manual QA, or another proportionate verification path.
- Stop and request direction when implementation reveals a material requirement change, unsafe side effect, or scope expansion.

## Choose Response Depth

- **Light**: one small area, simple validation, copy, styling, field plumbing, configuration, or minor CRUD. Give a compact judgment and next state.
- **Standard**: spans 2–4 layers, common business logic, API/UI integration, persistence, or meaningful verification. Use the full Advisory flow concisely.
- **Deep**: affects permissions, state transitions, consistency, migrations, async work, security, performance, compatibility, or multiple services. Compare real alternatives and cover rollback or degradation.

Do not force career analysis, solution alternatives, or long templates onto a Light request unless the user asks for them.

## Stage 1: Advisory

Complete Advisory before any delivery work. Keep it read-only and proportional to the selected depth.

### 1. Classify The Entry

- For a new requirement, enhancement, or defect-fix request, follow the full Advisory flow.
- For a value or feasibility question, finish with a decision and stop unless execution is also requested.
- For an implementation-plan question, produce a project-aware plan and stop unless execution is also requested.
- For a proposed solution, patch, diff, or PR, read [references/review-protocol.md](references/review-protocol.md) and perform Review. If the user then asks to implement fixes, use the findings as Advisory context and continue to the delivery gate without repeating the full analysis.

### 2. Inspect Instructions And Context

When a project is available:

1. Read repository instructions and relevant documentation.
2. Locate the entry point, domain path, data path, integrations, verification patterns, and project conventions.
3. Cite concrete files, modules, functions, or flows when available.

Remain framework-agnostic and state assumptions when the repository is unavailable. Ask at most two concise questions only when missing information blocks a responsible decision.

### 3. Normalize The Requirement

Capture only what matters:

- actor and problem;
- desired observable behavior;
- acceptance criteria;
- non-goals and scope boundary;
- permissions, invalid states, empty data, failures, concurrency, compatibility, performance, and consistency where relevant.

Propose reasonable acceptance criteria instead of blocking on every omission. Mark uncertain facts as assumptions.

### 4. Evaluate And Recommend

Evaluate project value, learning value, career potential, cost, dependencies, risks, and evidence strength. Read [references/value-rubric.md](references/value-rubric.md) when the user asks about value or career impact, or when the requirement is Standard or Deep.

Recommend one outcome:

- **Do now**
- **Split first**
- **Clarify first**
- **Defer**
- **Reject**

Do not invent business metrics, scale, performance gains, user impact, or personal contribution. Distinguish potential value from demonstrated evidence.

### 5. Outline The Solution

- Identify affected layers and the smallest design that satisfies the requirement.
- Compare alternatives only when a real tradeoff exists.
- Explain the main decision, affected areas, implementation sequence, risks, and verification strategy.
- Prefer project conventions over generic architecture advice.

### 6. Apply The Delivery Gate

- If the user requested only analysis, planning, diagnosis, or Review, finish Stage 1 and stop. Do not force an execution question.
- If the user already chose Manual or explicitly authorized Automatic delivery, continue with that strategy after Advisory.
- If implementation appears desired but no delivery strategy is selected, ask the user to choose:
  - **Manual**: the user writes code with step-by-step coaching;
  - **Automatic**: the agent implements within the approved scope;
  - **Stop**: retain the analysis or plan without implementation.
- Do not ask again when the user has already made an unambiguous choice.

## Stage 2: Delivery

### Manual

Before Manual delivery, read [references/manual-delivery.md](references/manual-delivery.md) completely. Keep the agent read-only, give one meaningful action at a time, review the user's result, and continue through verification.

### Automatic

Before Automatic delivery, read [references/automatic-delivery.md](references/automatic-delivery.md) completely. Confirm that explicit authorization exists, implement only the agreed scope, and verify proportionately.

Allow the user to switch strategies at any point. Switching from Manual to Automatic requires explicit authorization. Do not repeat Advisory unless the requirement, acceptance criteria, constraints, or scope changed materially.

## Stage 3: Verification And Learning Review

Verify against:

- acceptance criteria;
- relevant automated checks or the best permitted alternative;
- data and state edge cases;
- manual QA where useful;
- regression risks;
- logs, metrics, tracing, or rollback behavior when relevant.

Separate **passed**, **failed**, and **not run** checks. Never imply that unrun validation passed.

For substantial work, finish with:

- what changed or was decided;
- why the solution fits the project;
- what was verified and what remains uncertain;
- the main technical or domain lesson;
- credible resume or interview evidence, if any;
- the next useful learning step.

Keep this to one or two short points for Light work.

## Response Contract

Lead with the decision or most important finding. Include only sections that help the current decision; never fill a template mechanically.

For Advisory, usually cover:

1. requirement and assumptions;
2. decision and evidence confidence;
3. value, cost, and risks;
4. solution outline and verification;
5. next state: stop, clarify, Manual, or Automatic.

For Review, lead with actionable findings. For Manual, end with one concrete user action. For Automatic, summarize changed files and verification evidence without implying permission for Git or deployment operations.
