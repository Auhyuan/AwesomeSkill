# Value Rubric

Use this rubric for Standard or Deep requirements and whenever the user asks whether work is valuable, worth doing, useful for learning, or suitable for a resume or interview.

## Establish Evidence Confidence

Rate confidence before making a strong recommendation:

- **High**: the repository or specification is available, relevant flows were inspected, and claims are tied to concrete evidence.
- **Medium**: enough context exists for a useful judgment, but business impact, production constraints, ownership, or scale is partly inferred.
- **Low**: only a brief description is available. Give a preliminary judgment and list the evidence needed to improve it.

Use **unknown** instead of forcing a rating when evidence is insufficient.

## Evaluate Project Value

Rate project value as high, medium, or low using these factors:

- importance of the affected workflow;
- correctness, security, permission, reliability, performance, observability, or operational improvement;
- user or team friction removed;
- reuse across features or modules;
- urgency, dependencies, implementation cost, and regression risk.

Do not equate technical complexity with project value. Small changes can have high value when they remove real risk or recurring friction.

## Evaluate Learning Value

Consider:

- technical depth: domain modeling, state transitions, transactions, consistency, concurrency, performance, security, debugging, or observability;
- technical breadth: meaningful work across UI, API, domain, persistence, integrations, delivery, or operations;
- transferability to other systems and roles;
- degree of reasoning, ownership, and feedback available to the user.

Distinguish exposure from learning. Seeing a technology is exposure; making and verifying a consequential decision with it is learning.

## Evaluate Career Potential

Separate potential from evidence:

- **Potential**: whether the work could form a story about a real problem, constraints, alternatives, implementation, verification, and outcome.
- **Current evidence**: concrete artifacts such as code ownership, design decisions, tests or checks, incident reduction, measured behavior, review feedback, or released impact.
- **Evidence gap**: what must still be captured before making a strong resume or interview claim.

Use:

- **Strong potential**: meaningful ownership and tradeoffs can produce a differentiated, evidence-backed story.
- **Moderate potential**: useful project familiarity or engineering practice, but impact or ownership evidence is limited.
- **Weak potential**: too small or repetitive to stand alone; combine it with adjacent work or describe it as onboarding and execution practice.

Never fabricate metrics, production scale, user impact, or the user's contribution. Suggest what to measure instead.

## Produce A Decision

Recommend one of:

- **Do now**: value and timing justify the cost.
- **Split first**: a smaller slice can validate assumptions or reduce risk.
- **Clarify first**: missing information materially changes the design or value.
- **Defer**: useful, but dependencies, timing, or opportunity cost make it premature.
- **Reject**: expected value is too low or the approach creates unacceptable risk.

State the rating, evidence, uncertainty, and reason. A low-value requirement can still be worthwhile for onboarding, pattern learning, accessibility, or reducing product friction.
