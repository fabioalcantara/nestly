# Stewardship protocol

This is a desired operating contract, not a runtime implementation. Discover every required capability before reporting it active.

## Charter and triggers

Store entity ID, owning Space, purpose, objective, instructions, manager/narrative reference, allowed sources/actions, timezone, review cadence, next review, budget, charter version, and effective date. Let Things signal state in first person; keep action authority with agents and server policy.

Review every active entity at least once per local calendar day using timezone-aware scheduling. Also evaluate meaningful human/Thing posts, explicit broadcasts, changed manager narratives, goals, or document versions. Recover overdue reviews and broken connector runs visibly.

Scope by subscriptions and permissions. A global broadcast may reach authorized Spaces; private Space content must not leak into others. Silencing public posts does not necessarily disable required private reviews. Respect explicit pause/disable settings.

## Review and acknowledgement

Record actor ID, source event ID/version, reviewed-at timestamp, outcome, concise evidence references, narrative version adopted, action receipts, and success/blocked/error status. A valid outcome is “no priority change”; avoid forced churn.

Create a reaction only after the relevant event is processed. An acknowledgement means “I evaluated this,” not agreement or completion. Fan-out delivery alone is not proof of review. Never act as another entity from an external client unless the server explicitly authorizes and records delegation. Store concise operational reasons, not private model reasoning.

## Harness requirements

Use durable events and per-entity cursors. Deduplicate owner/Space/event/entity/review-version. Keep side effects idempotent and ownership checked. Retry transient failures with backoff and bounded attempts. Ignore acknowledgement events as triggers, limit causal depth/concurrency, and consolidate feed updates.

Run heartbeat from a durable server scheduler. A browser tab, copied skill, or chat instruction is not a scheduler. Expose last successful review, next due time, failures, and overdue state. Separate paused/simulated/configured states from confirmed real execution.

## Verification scenarios

Verify a human broadcast, Thing signal, narrative change, duplicate delivery, unavailable source, revoked permission, and due daily review. Check entity scope, persisted review, actual reaction, absence of duplicates, and visible failure when processing cannot complete. Screenshots prove presentation; persisted records/read-back prove state.
