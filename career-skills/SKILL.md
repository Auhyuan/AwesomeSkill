---
name: career-skills
description: Route software-engineering career-growth requests to the appropriate specialized workflow. Use when the user wants to evaluate a software project's learning, technical, resume, interview, job-switching, or re-employment value; or when they want guided analysis and implementation of a new feature requirement with explicit project, learning, and career value. Also use when the request combines project evaluation with requirement-delivery guidance.
---

# Career Skills Router

Identify the user's intent, load only the matching child workflow, and then follow that workflow completely. Treat child `SKILL.md` files as executable instructions, not as background material to summarize.

## Route The Request

- For whole-project, repository, system, module, internship, company-project, side-project, or open-source value assessment, read [`project-evaluation/SKILL.md`](project-evaluation/SKILL.md) completely and follow it.
- For a new feature, product change, enhancement, implementation task, or guided requirement delivery, read [`requirement-helper/SKILL.md`](requirement-helper/SKILL.md) completely and follow it.
- For a mixed request, choose the workflow that matches the user's immediate goal first. Load the second workflow only when its output is necessary to complete the same request.

## Routing Boundaries

- Route project-level judgments to `project-evaluation`; do not replace them with a feature-level value assessment.
- Route implementation guidance to `requirement-helper`; do not let project scoring replace requirement analysis, acceptance criteria, planning, or verification.
- Do not duplicate the child workflows in this file.
- Do not load both child workflows by default. Preserve context by loading the minimum required instructions.
- If neither workflow applies, state that this skill collection does not cover the request and continue using the agent's normal capabilities or another applicable skill.

## Combined Requests

When both workflows are required:

1. Use `project-evaluation` to establish project-level value, evidence strength, and high-value opportunity areas.
2. Use `requirement-helper` to analyze and deliver the concrete requirement.
3. Carry forward only conclusions relevant to the requirement; do not repeat the complete project evaluation.

