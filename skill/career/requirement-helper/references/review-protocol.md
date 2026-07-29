# Review Protocol

Use this protocol when the user provides a solution, implementation plan, patch, diff, PR, or completed Manual step for evaluation.

## Keep Review Read-Only

- Inspect relevant project context and repository instructions.
- Do not edit files unless the user later gives explicit Automatic-delivery authorization.
- Review the artifact the user supplied, not an imagined implementation.
- State when missing context limits confidence.

## Review In Risk Order

Lead with actionable findings:

- **P0 — Critical**: data loss, security exposure, severe permission bypass, unrecoverable production impact, or a fundamentally invalid design.
- **P1 — Must fix**: correctness failure, broken acceptance criterion, compatibility break, race condition, or likely regression.
- **P2 — Should improve**: maintainability problem, brittle design, important missing verification, inefficient data access, or unclear ownership.
- **P3 — Optional**: local clarity, naming, simplification, or polish with limited risk.

For each finding:

1. identify the concrete file, function, behavior, or plan step;
2. explain the failure scenario or cost;
3. connect it to the requirement or engineering principle;
4. recommend the smallest practical correction;
5. state confidence when evidence is incomplete.

Avoid presenting personal style preferences as correctness defects.

## Review By Artifact Type

For a plan or design, check:

- requirement coverage and non-goals;
- ownership and layer boundaries;
- data, permission, state, compatibility, and operational risks;
- realistic sequencing, rollback, and verification.

For code or a diff, check:

- correctness and edge cases;
- consistency with project patterns;
- data access, transactions, concurrency, and error handling;
- API or schema compatibility;
- verification gaps and regression risk;
- unnecessary scope expansion.

## Finish

- Separate must-fix findings from optional improvements.
- If no actionable defect is found, say so directly and list residual risks or unverified areas.
- End with a short prioritized checklist.
- If the user asks the agent to implement fixes, reuse the review as Advisory context, apply the delivery gate, and avoid repeating the full analysis.
