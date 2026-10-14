# Connect to Nestly over MCP

Nestly exposes one remote MCP server. Claude, Cursor, ChatGPT, and other standard MCP clients connect to it with OAuth 2.1.

The public connection guide is [https://nestly.bot/connect/mcp](https://nestly.bot/connect/mcp).

## Endpoint

| Role | URL |
| --- | --- |
| Canonical MCP endpoint | `https://nestly.bot/api/mcp` |
| Alias, once deployed | `https://nestly.bot/mcp` |

The transport is Streamable HTTP. Configure the client with the canonical URL.

## Authorization

The authorization server issuer is `https://nestly.bot`. Clients use the authorization-code grant with PKCE `S256` and dynamic client registration. The token endpoint accepts public clients (`none`). Supported grants are `authorization_code` and `refresh_token`.

| Purpose | URL |
| --- | --- |
| Dynamic client registration | `https://nestly.bot/oauth/register` |
| Authorization | `https://nestly.bot/oauth/authorize` |
| Token | `https://nestly.bot/oauth/token` |
| Authorization server metadata | `https://nestly.bot/.well-known/oauth-authorization-server` |
| Protected resource metadata | `https://nestly.bot/.well-known/oauth-protected-resource/api/mcp` |

Published scopes are `nestly:read` and `nestly:write`.

Any safe `https` redirect URI registered through dynamic client registration is accepted. Loopback redirects are accepted. Each person authorizes their own account. Never share API keys, authorization codes, or tokens in a prompt.

## Membership

Magic-link sign-in works for members. An administrator grants access from Inbox with **Conceder entrada por email** (action `grant`). After that grant, the member can finish magic-link sign-in and authorize the MCP client.

## Verify access

Follow the MCP setup flow published for the client in use. A pasted prompt does not install a connector. After authorization, ask for a Space list. An empty list is a successful read. A website login or an OAuth success screen still needs that read before the connection counts as working in the conversation.

The [connection prompt](../prompts/connect.txt) asks for that read-only check.
