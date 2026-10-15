---
name: nestly-connect-verify
description: Connect an account to Nestly and verify real MCP access. Use for first connection, authorization, missing Nestly actions, reconnection, or a read-only connection check in Claude, Cursor, ChatGPT, or another standard MCP client.
---

# Connect and verify Nestly

Respond in the user's language. Distinguish installation, OAuth authorization, tool availability, and a successful account read. A copied prompt, browser login, or OAuth success screen is not proof of operational MCP access.

1. Discover the Nestly tools actually exposed in this conversation. Match server and descriptions, not similar names from another plugin. Read live schemas.
2. If tools are absent, use an advertised connection capability if available. Otherwise guide the user through the client's supported MCP setup one step at a time. Verify current official instructions when uncertain; ask what the user sees instead of inventing controls.
3. Use these public details. Name: Nestly. Canonical endpoint: https://nestly.bot/api/mcp (Streamable HTTP). Alias once deployed: https://nestly.bot/mcp. Authorization: OAuth 2.1 with PKCE S256 and dynamic client registration at https://nestly.bot/oauth/register, https://nestly.bot/oauth/authorize, and https://nestly.bot/oauth/token. Scopes: nestly:read and nestly:write. Any safe https redirect URI registered through dynamic client registration is accepted, and loopback redirects are accepted, so Claude, Cursor, ChatGPT, and other standard MCP clients can connect. Public guide: https://nestly.bot/connect/mcp. Request read access for this test; accept a client that requests the published combined scope bundle after user consent.
4. Magic-link sign-in works for members. When the address is not a member, an admin grants access from Inbox with Conceder entrada por email (action grant). Leave login and authorization to the user. Never request, store, or echo passwords, authorization codes, tokens, or API keys. Do not import chat history or personal memories.
5. When `list_spaces` is exposed, call it without mutation. Report the real count and relevant returned names. An empty list is a successful read and valid new-account state.
6. If `get_capabilities` is exposed, inspect it to distinguish enabled, simulated, and unavailable features. Do not assume that website and remote connector capabilities are identical.
7. If authorization succeeded but tools remain absent, report the last verified stage. After a documented server update, refresh existing connection metadata and test a new conversation where supported. Avoid repeated login or recreating connections without evidence.

Preserve non-sensitive error categories and safe request identifiers. Do not retry a 401 indefinitely, bypass authentication, switch users, or call a browser fallback and report it as MCP success.

Finish with one of: verified read access; authorized but tools unavailable; authorization required; membership grant required; or connection failed with actual reason. This workflow creates or changes nothing. Receiving a skill does not install a connection or run a background service.

