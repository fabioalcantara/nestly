# Nestly integration skills

Nestly keeps context, intentions, goals, people, agents, and living Things together. This public package teaches an external assistant how to work with Nestly reliably. It contains no private application source, account data, tokens, or production screenshots.

## Four workflows

- **Connect and verify**: distinguish authorization from real tool access; test with a read-only Space list.
- **Launch an opportunity**: evaluate a business idea, design a paid-pilot experiment, and create/read back an authorized Space.
- **Evolve a Space**: preserve document versions, agent charters, and partial execution history.
- **Stewardship**: review daily behavior and change/broadcast acknowledgements without inventing background execution.

Skills guide an assistant. Nestly's server supplies permissions, data, execution, and scheduling. Installing this package does not create those server capabilities.

## Connect your account

Use [Nestly's connection page](https://nestly.bot/connect/chatgpt). The remote MCP endpoint is `https://nestly.bot/mcp`, authenticated with OAuth and dynamic client registration. Published scopes are `nestly:read` and `nestly:write`. Every user authorizes their own account; never share API keys or tokens in a prompt.

If your ChatGPT account supports custom MCP connections, follow the current [official quickstart](https://developers.openai.com/plugins/quickstart). Menu availability depends on the client, account, and administrator. A pasted prompt cannot install a connector or guarantee that its tools are exposed. The [connection prompt](prompts/connect-pt-BR.txt) guides setup and verifies a real read without creating anything.

After authorization, enable the connection in the conversation and request a Space list. An empty list is a successful test. If tools are absent, report that stage; a successful website login does not establish MCP access. After server metadata changes, follow the client's refresh procedure and retest.

## Use this package

The root `plugin.json`, `mcp.json`, and `skills/` follow the portable Agent Plugins package format described in [OpenAI's packaging guide](https://developers.openai.com/plugins/build/plugins). No user-specific development connector ID is embedded.

For a Codex installation that supports Git marketplaces, add this repository as a marketplace source:

```sh
codex plugin marketplace add fabioalcantara/nestly --ref main
```

Then inspect and install Nestly from that source using the client's supported plugin UI and authorize OAuth. Adding a marketplace is not the same as installing or authorizing its plugin. The repository also includes a repo-scoped marketplace catalog for compatible clients.

For clients that import individual skills, choose a complete folder under `skills/` and connect the MCP server separately. Import support differs across clients. Ask the assistant to use one of the named workflows once it is available.

This repository is a distributable source package, not evidence of approval in the public ChatGPT plugin directory. Directory publication and an end-to-end installation test are separate release gates. In clients that cannot import it, the plain-text prompts remain usable as instructions, with the same capability checks.

## Runtime compatibility

Always discover live tools and schemas. The baseline includes Space/agent/Thing reads and writes, context delivery, and proposed tasks. Newer servers may expose capabilities and durable plan execution. A skill mentions those tools conditionally and must verify them before use.

- `send_to_nestlybot` delivers context; it does not execute the enclosed instructions.
- `create_task` proposes a task; it is not a background schedule.
- A saved or simulated schedule is not a verified autonomous run.
- An acknowledgement means an entity evaluated an event; it is distinct from agreement or task completion.
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
