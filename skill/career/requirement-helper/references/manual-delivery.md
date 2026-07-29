# Manual Delivery

Use Manual delivery when the user wants to write the code, learn the project, or be guided step by step.

## Preserve The Boundary

- Keep the agent read-only unless the user explicitly switches to Automatic delivery.
- Do not silently implement the solution, edit files, or make external changes.
- Small examples, pseudocode, or focused snippets are allowed when they clarify the current step.
- Respect repository instructions and the verification constraints established during Advisory.

## Use A Coaching Loop

1. Reuse the Advisory result instead of repeating it.
2. Explain the current code path, the purpose of the next change, and the relevant target file or function.
3. Give exactly one meaningful action or reasoning task.
4. Let the user attempt it and ask them to share the diff, code, error, output, or conclusion.
5. Review the result with concrete feedback:
   - correctness;
   - design fit;
   - edge cases;
   - maintainability;
   - verification.
6. Continue with the next smallest meaningful action.

Do not break work into trivial keystrokes. Each step should teach one coherent idea and produce something reviewable.

## Escalate Help Gradually

Use the smallest level of help that unblocks learning:

1. a focused question;
2. a conceptual hint;
3. pseudocode or data flow;
4. a small illustrative snippet;
5. a fuller example only after the user is blocked or explicitly requests it.

Avoid turning checkpoint questions into a quiz. Ask them only when the answer changes the design or teaches an important project concept.

Useful checkpoints include:

- Which layer owns this rule, and why?
- Which state, permission, consistency, or compatibility boundary can fail?
- What is the smallest useful verification for this change?
- What evidence will prove the acceptance criterion?

## Handle Strategy Changes

- Continue Manual delivery without reconfirming after each step.
- Switch to Automatic only after explicit user authorization.
- Return to Advisory when the user changes the requirement, acceptance criteria, or scope materially.

## Finish

Complete the loop through verification. Summarize what the user implemented, the important decision they made, the evidence that it works, and the next learning opportunity.

Until the work is complete, end each response with one concrete next user action.
