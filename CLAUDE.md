# Claude instructions for Nestly

## Mandatory bootstrap check

Before you create a new project, application, service, worker, agent system, MCP server, mobile client, data workload, or substantially re-scaffold an existing project, read:

- `docs/quick-start-blueprint-library.md`

Prefer a canonical, maintained foundation over rebuilding commodity scaffolding. Choose the smallest suitable blueprint, compose multiple blueprints only when their responsibilities are distinct, and record upstream sources plus important deviations.

Do not blindly fork or copy a starter. Verify maintenance, licensing, dependencies, security posture, buildability, and fit. Preserve Nestly-specific logic behind portable interfaces where practical.

A bootstrap is not complete until its build/run path, tests, thin-slice behavior, agent instructions, and acceptance evidence are verified.

For non-bootstrap work, follow the existing repository contract in `docs/contract.md`.
