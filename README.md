# Nestly integration skills

Nestly keeps context, intentions, goals, people, agents, and living Things together. This public package teaches an external assistant how to work with Nestly reliably. It contains no private application source, account data, tokens, or production screenshots.

## Four workflows

- **Connect and verify**: distinguish authorization from real tool access; test with a read-only Space list.
- **Launch an opportunity**: evaluate a business idea, design a paid-pilot experiment, and create/read back an authorized Space.
- **Evolve a Space**: preserve document versions, agent charters, and partial execution history.
- **Stewardship**: review daily behavior and change/broadcast acknowledgements without inventing background execution.

Skills guide an assistant. Nestly's server supplies permissions, data, execution, and scheduling. Installing this package does not create those server capabilities.

## Connect your account

Use the [public MCP guide](https://nestly.bot/connect/mcp). The same connection contract is written up in [the MCP guide in this repository](docs/mcp.md).

The canonical remote endpoint is `https://nestly.bot/api/mcp` (Streamable HTTP). `https://nestly.bot/mcp` is an alias of that endpoint once the alias is deployed. Configure clients with the canonical URL.

Authorization is OAuth 2.1 with PKCE (`S256`) and dynamic client registration:

- Register a client at `https://nestly.bot/oauth/register`
- Authorize at `https://nestly.bot/oauth/authorize`
- Exchange tokens at `https://nestly.bot/oauth/token`

Published scopes are `nestly:read` and `nestly:write`. Any safe `https` redirect URI registered through dynamic client registration is accepted, and loopback redirects are accepted. Claude, Cursor, ChatGPT, and other standard MCP clients can connect. Every person authorizes their own account. Never share API keys or tokens in a prompt.

Magic-link sign-in works for members. An admin grants access from Inbox with **Conceder entrada por email** (action `grant`).

Follow the MCP setup flow published for the client in use. Menu availability depends on the client, account, and administrator. A pasted prompt cannot install a connector or guarantee that its tools are exposed. The [connection prompt](prompts/connect.txt) guides setup and verifies a real read without creating anything.

After authorization, enable the connection in the conversation and request a Space list. An empty list is a successful test. If tools are absent, report that stage. A successful website login does not establish MCP access. After server metadata changes, follow the client's refresh procedure and retest.

## Use this package

The root `plugin.json`, `mcp.json`, and `skills/` follow the portable Agent Plugins package format described in [OpenAI's packaging guide](https://developers.openai.com/plugins/build/plugins). No user-specific development connector ID is embedded.

For a Codex installation that supports Git marketplaces, add this repository as a marketplace source:

```sh
codex plugin marketplace add fabioalcantara/nestly --ref main
```

Then inspect and install Nestly from that source using the client's supported plugin UI and authorize OAuth. Adding a marketplace is not the same as installing or authorizing its plugin. The repository also includes a repo-scoped marketplace catalog for compatible clients.

For clients that import individual skills, choose a complete folder under `skills/` and connect the MCP server separately. Import support differs across clients. Ask the assistant to use one of the named workflows once it is available.

This repository is a distributable source package. Directory publication and an end-to-end installation test are separate release gates. In clients that cannot import it, the plain-text prompts remain usable as instructions, with the same capability checks.

## Project bootstrap blueprints

For new applications, services, workers, agent systems, MCP servers, mobile clients, data workloads, or major re-scaffolds, Codex, Claude, and other implementation agents must consult [the Quick-Start Blueprint Library](docs/quick-start-blueprint-library.md) before selecting a framework or generating a scaffold.

The library favors a small set of maintained, composable upstream foundations rather than starting from zero or accumulating near-duplicate boilerplates. Root `AGENTS.md` and `CLAUDE.md` make this bootstrap check explicit for their respective agents.

Selections should be intent-first. Record upstream sources and important deviations, verify maintenance and licensing, and treat the agent harness, tests, build path, thin-slice validation, and acceptance evidence as part of the project foundation.

## Runtime compatibility

Always discover live tools and schemas. The baseline includes Space/agent/Thing reads and writes, context delivery, and proposed tasks. Newer servers may expose capabilities and durable plan execution. A skill mentions those tools conditionally and must verify them before use.

- `send_to_nestlybot` delivers context; it does not execute the enclosed instructions.
- `create_task` proposes a task; it is not a background schedule.
- A saved or simulated schedule is not a verified autonomous run.
- Distinguish received/queued acknowledgements from reviewed events. Only a completed evaluation record proves review; neither state implies agreement or task completion.
- A screenshot shows visible state; receipts and read-back verify persisted results.

See [the contract guidance](docs/contract.md) and [evaluation scenarios](tests/scenarios.json).

## Validate and evaluate

Run the dependency-free checks with Python 3.10 or later:

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

These checks validate package structure, metadata, references, and test-fixture integrity. They do not prove model quality, OAuth connectivity, tenant isolation, scheduled execution, or successful installation. Use the scenario fixture for forward tests with a model and recorded tool results. Keep live evidence private and redact it before public sharing.

Contributions should preserve idempotency, explicit capability checks, owner/Space boundaries, source provenance, and accurate completion claims. Never commit customer data or credentials. A skill is not a way to bypass the server's permissions.
