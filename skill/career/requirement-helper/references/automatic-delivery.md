# Automatic Delivery

Use Automatic delivery only after the user explicitly authorizes the agent to modify code for the current requirement.

## Confirm Scope And Authority

- Reuse the Advisory result and agreed acceptance criteria.
- Verify that repository instructions were read.
- Treat code-edit permission as separate from permission to stage, commit, push, deploy, migrate production data, or perform external writes.
- Let explicit exclusions and no-change instructions override broader implementation language.
- Stop when a discovered dependency or side effect materially expands the approved scope.

## Implement Deliberately

1. State a concise implementation plan before editing. Do not repeat the full Advisory analysis.
2. Inspect the relevant code path and preserve existing user changes.
3. Make the smallest coherent change that satisfies the acceptance criteria and project conventions.
4. Explain an important design decision when a real alternative or tradeoff exists.
5. Keep documentation, configuration, migrations, and generated artifacts within the approved scope.

Do not manufacture work merely to fill an implementation template.

## Verify Proportionately

Choose the strongest permitted evidence available:

1. focused existing tests or checks;
2. relevant build or compilation;
3. static analysis, linting, type checking, or schema validation;
4. targeted manual QA;
5. code-path inspection when execution is unavailable.

Add tests only when they are valuable and allowed by user and repository instructions. If new tests are forbidden, do not generate test files; use the best alternative verification and state the limitation.

Report checks as:

- **Passed**
- **Failed**
- **Not run**, with the reason and next best verification path

Never claim completion solely because code was edited.

## Handle Changes During Delivery

- Continue without another mode question when implementation remains inside the approved requirement.
- Return to Advisory when acceptance criteria, constraints, or scope change materially.
- Ask for new authority before destructive actions, production changes, external side effects, or Git operations not explicitly requested.

## Finish

Summarize:

- what changed and where;
- why it satisfies the requirement;
- verification evidence and remaining uncertainty;
- important tradeoffs or rejected alternatives, when relevant;
- learning and credible career evidence for substantial work.

Do not stage, commit, push, or deploy unless the user separately requested that action.
