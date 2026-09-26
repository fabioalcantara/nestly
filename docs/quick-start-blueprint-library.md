# Quick-Start Blueprint Library

Status: canonical project-bootstrap reference for Nestly agents and contributors.

## Purpose

Before starting a new application, service, agent system, MCP server, worker, mobile client, data project, or other major scaffold, check this library first.

The goal is not to collect boilerplate. The goal is to give Codex, Claude, and other implementation agents known-good foundations so they spend effort on product behavior, context, tests, and differentiation instead of repeatedly rebuilding commodity scaffolding.

A blueprint may be composed from multiple upstream foundations. Do not blindly fork a starter and treat its architecture as a product requirement.

## Bootstrap doctrine

For every new-project or major-rescaffold task:

1. Read this document before choosing a stack or creating files.
2. Identify the project intent and select the smallest suitable canonical blueprint.
3. Check whether two or more blueprints should be composed instead of forcing one starter to cover everything.
4. Verify the upstream repository is still maintained, review its license, and inspect its current security/dependency posture before adoption.
5. Record the selected blueprint(s), upstream URL, pinned commit/tag when practical, and important deviations in the new project's bootstrap notes.
6. Import patterns and capabilities deliberately. Do not copy secrets, environment files, CI credentials, issue history, telemetry identifiers, or unrelated product code.
7. Keep Nestly-specific domain logic outside vendor-specific adapters where practical.
8. Add or preserve an agent harness: durable instructions, goals/plans, tests, acceptance evidence, and implementation receipts.
9. Prefer a working end-to-end thin slice over a large generated scaffold with unverified surfaces.
10. If no blueprint fits, document the gap so the library can evolve rather than silently starting from zero.

## Canonical blueprints

### BPT-WEB-SAAS — Production web / SaaS

Primary foundation:
- Vercel next-forge: https://github.com/vercel/next-forge

Use for:
- multi-surface web products
- SaaS applications
- products needing a mature monorepo, design system, auth, database, email, docs, and deployment conventions

Lighter alternative:
- Next.js SaaS Starter: https://github.com/nextjs/saas-starter

Use the lighter alternative when the product does not need next-forge's broader monorepo surface.

### BPT-TS-WEB — Lean TypeScript web app

Primary foundation:
- create-t3-app: https://github.com/t3-oss/create-t3-app

Use for:
- TypeScript-first applications
- smaller services or products where a highly opinionated SaaS monorepo would add unnecessary weight

### BPT-AI-WEB — AI-native conversational application

Primary foundation:
- Vercel Chatbot: https://github.com/vercel/chatbot

Use for:
- AI-first web applications
- conversational UX
- streaming model interactions
- products where chat is a primary surface rather than an add-on

Compose with BPT-WEB-SAAS when commercial SaaS capabilities are also required.

### BPT-CHATGPT-APP — ChatGPT application / interactive MCP experience

Primary foundation:
- OpenAI Apps SDK examples: https://github.com/openai/openai-apps-sdk-examples

Use for:
- ChatGPT apps
- MCP-backed interactive widgets
- authenticated ChatGPT experiences
- stateful cards, maps, or other app surfaces

Treat examples as reference implementations, not a reason to couple Nestly core logic to a ChatGPT-only runtime.

### BPT-AGENT-RUNTIME — Agent system

Primary foundations:
- OpenAI Agents SDK for JavaScript: https://github.com/openai/openai-agents-js
- OpenAI Agents SDK for Python: https://github.com/openai/openai-agents-python

Use for:
- tool-using agents
- handoffs
- sessions
- tracing
- multi-agent orchestration

Choose the language that matches the surrounding system. Keep domain protocols model- and vendor-portable where practical.

### BPT-API-PY — Python API / service

Primary foundation:
- FastAPI full-stack template: https://github.com/fastapi/full-stack-fastapi-template

Use for:
- API services
- Python-heavy backends
- service layers
- products requiring PostgreSQL, tests, browser tests, containerization, and CI conventions

For Nestly, this is a strong candidate for independent services behind the Experience/API boundary.

### BPT-MOBILE — Cross-platform mobile application

Primary foundation:
- Expo: https://github.com/expo/expo

Bootstrap with the current create-expo-app recommendations.

Use for:
- iOS
- Android
- shared web/mobile experiences
- agent-assisted mobile development

Preserve a clean boundary between device UX and Nestly APIs so native clients can coexist later.

### BPT-DATA-AI — Databricks data / intelligence project

Primary foundation:
- Databricks CLI / Asset Bundle templates: https://github.com/databricks/cli

Use for:
- Databricks jobs
- governed data/AI workloads
- deployment bundles
- Lakehouse/Lakebase-adjacent project scaffolding
- data intelligence and model-serving workloads

Do not make Databricks-specific implementation details leak into client experience contracts unless required.

### BPT-CLAUDE-APP — Claude-native reference application

Primary foundation:
- Anthropic Claude Quickstarts: https://github.com/anthropics/claude-quickstarts

Use for:
- Claude-specific experiments
- reference patterns for Claude-powered applications
- comparison or portability testing

Prefer portable Nestly contracts over Claude-specific assumptions in core architecture.

### BPT-CLAUDE-SKILL — Claude capability / behavior package

Primary foundation:
- Anthropic Skills: https://github.com/anthropics/skills

Use for:
- reusable Claude skills
- packaged operational guidance
- capability-specific instructions and examples

### BPT-AGENT-HARNESS — Codex / Claude operating harness

Reference foundations:
- OpenAI Cookbook Codex development workflow:
  https://github.com/openai/openai-cookbook/blob/main/examples/codex/iterating-development-workflows-with-codex.md
- Anthropic Claude Code:
  https://github.com/anthropics/claude-code

Every substantial project should have an agent-operable harness appropriate to its runtime, typically including:

- `AGENTS.md`
- `CLAUDE.md` when Claude is expected to work in the repository
- goals and plans
- durable architectural decisions
- acceptance criteria
- automated tests
- verification/evidence expectations
- build/run instructions
- clear boundaries around secrets and destructive operations

The harness is part of the product foundation, not optional documentation added after implementation.

## Intent-first selection

Start with intent, not framework preference.

Typical mappings:

- Commercial web SaaS -> BPT-WEB-SAAS
- Lean TypeScript product -> BPT-TS-WEB
- AI-first conversational product -> BPT-AI-WEB
- ChatGPT-native surface -> BPT-CHATGPT-APP
- Tool-using or multi-agent service -> BPT-AGENT-RUNTIME
- Python API/runtime -> BPT-API-PY
- iOS/Android shared client -> BPT-MOBILE
- Databricks intelligence/data workload -> BPT-DATA-AI
- Claude-specific capability -> BPT-CLAUDE-APP or BPT-CLAUDE-SKILL
- Any substantial repository -> compose with BPT-AGENT-HARNESS

## Composition example

A Nestly-like multi-tenant AI product might compose:

- BPT-WEB-SAAS for the conventional application shell
- BPT-AI-WEB for streaming/conversational experience patterns
- BPT-AGENT-RUNTIME for agent execution
- BPT-API-PY for an independent service boundary where Python is advantageous
- BPT-DATA-AI for Databricks workloads
- BPT-AGENT-HARNESS for Codex/Claude operability

The result is a new product architecture informed by these references, not a pile of copied repositories.

## Acceptance gate

A bootstrap is not complete merely because generation succeeded.

Before declaring the foundation ready, verify at least:

- clean install from documented prerequisites
- build succeeds
- tests run
- lint/type checks run where applicable
- application starts locally
- one end-to-end thin slice works
- secrets are externalized
- dependency/licensing review is recorded
- selected blueprint sources are recorded
- agent instructions point back to this library
- deviations from the blueprint are explicit

## Library stewardship

This library is curated, not exhaustive.

When a materially better upstream foundation emerges:
1. compare it with the current canonical choice,
2. validate maintenance, license, security, architecture, and agent ergonomics,
3. run a representative bootstrap,
4. replace or add it deliberately,
5. record why.

Do not accumulate dozens of near-duplicate starters. Prefer a small set of strong, composable foundations.
