# ⚡ Awesome Agentic Patterns & Production Playbook

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/DYNOSuprovo/awesome-agentic-patterns?style=social)](https://github.com/DYNOSuprovo/awesome-agentic-patterns)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Agent Ecosystem](https://img.shields.io/badge/Agents-Claude%20%7C%20Cursor%20%7C%20Antigravity%20%7C%20Swarm-orange)](https://github.com/DYNOSuprovo/awesome-agentic-patterns)

> A curated collection of battle-tested **AI Agent architectures, Model Context Protocol (MCP) servers, system prompt blueprints, context window optimization strategies, and ready-to-use rule templates** for production software engineering.

---

## 📑 Table of Contents

- [Architectural Patterns](#-architectural-patterns)
  - [1. Supervisor / Hierarchical Delegation](#1-supervisor--hierarchical-delegation)
  - [2. Peer-to-Peer Swarm / Handoff](#2-peer-to-peer-swarm--handoff)
  - [3. Plan-and-Execute (Planner + Workers)](#3-plan-and-execute-planner--workers)
  - [4. Reflection & Evaluator-Optimizer](#4-reflection--evaluator-optimizer)
- [Curated Model Context Protocol (MCP) Directory](#-curated-model-context-protocol-mcp-directory)
- [Ready-to-Use Agent Configuration Blueprints](#-ready-to-use-agent-configuration-blueprints)
  - [Cursor (`.cursorrules`)](#cursor-cursorrules)
  - [Claude Code (`CLAUDE.md`)](#claude-code-claudemd)
  - [Google Antigravity (`AGENTS.md`)](#google-antigravity-agentsmd)
  - [Windsurf (`.windsurfrules`)](#windsurf-windsurfrules)
- [Context Window & Token Economics](#-context-window--token-economics)
- [Interactive Setup CLI](#-interactive-setup-cli)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🏛️ Architectural Patterns

```
                          ┌───────────────────────┐
                          │   USER PROMPT / TASK  │
                          └───────────┬───────────┘
                                      │
                                      ▼
                      ┌───────────────────────────────┐
                      │    SUPERVISOR / ROUTER AGENT  │
                      └───────┬───────────────┬───────┘
                              │               │
             ┌────────────────▼───┐       ┌───▼────────────────┐
             │ RESEARCH SUBAGENT  │       │ CODING SUBAGENT    │
             │ (Read-Only Tools)  │       │ (Read/Write/Exec)  │
             └────────────────┬───┘       └───┬────────────────┘
                              │               │
                              └───────┬───────┘
                                      │
                                      ▼
                      ┌───────────────────────────────┐
                      │     EVALUATOR & VERIFIER      │
                      └───────────────────────────────┘
```

### 1. Supervisor / Hierarchical Delegation
* **When to use:** Complex workflows where a primary agent breaks problems into sub-problems and delegates to specialized subagents.
* **Benefits:** Prevents context window dilution. The root agent receives only distilled summaries while subagents perform noisy intermediate tasks (e.g., searching 50 files or parsing massive logs).
* **Reference Template:** [`templates/antigravity/AGENTS.md`](templates/antigravity/AGENTS.md)

### 2. Peer-to-Peer Swarm / Handoff
* **When to use:** Multi-domain tasks where execution flow transitions statefully (e.g., Triage Agent $\to$ Billing Agent $\to$ Technical Agent).
* **Benefits:** Decentralized control; agents hand off control via structured function calling (`transfer_to_billing()`).

### 3. Plan-and-Execute (Planner + Workers)
* **When to use:** Long-running coding refactors or multi-module migrations.
* **Pattern:**
  1. **Planner Agent:** Creates an explicit step-by-step checklist (`task.md`).
  2. **Worker Agents:** Pick up sequential tasks and report status.
  3. **Verification Step:** Runs unit tests and linter before marking steps as completed.

### 4. Reflection & Evaluator-Optimizer
* **When to use:** Generating code, database security rules, or high-reliability API schemas.
* **Pattern:** Generator agent outputs draft $\to$ Critic/Auditor agent evaluates against security checklist $\to$ Generator applies targeted corrections.

---

## 🔌 Curated Model Context Protocol (MCP) Directory

The **Model Context Protocol (MCP)** standardizes how AI agents communicate with external tools and data sources. Below are production-ready MCP servers:

| MCP Server | Category | Description | Command / Source |
| :--- | :--- | :--- | :--- |
| **`mcp-server-filesystem`** | Filesystem | Secure, constrained file reading & editing | `npx -y @modelcontextprotocol/server-filesystem /path` |
| **`mcp-server-git`** | Version Control | Inspect diffs, commits, branches, and git logs | `uvx mcp-server-git` |
| **`mcp-server-postgres`** | Database | Read schemas and execute read-only queries | `npx -y @modelcontextprotocol/server-postgres <conn-string>` |
| **`mcp-server-github`** | Cloud / DevOps | Manage issues, pull requests, and discussions | `npx -y @modelcontextprotocol/server-github` |
| **`mcp-server-sqlite`** | Database | Local SQLite database introspection | `uvx mcp-server-sqlite --db-path <path>` |
| **`mcp-server-puppeteer`** | Web Automation | Browser navigation, screenshots, and scraping | `npx -y @modelcontextprotocol/server-puppeteer` |
| **`chrome-devtools-mcp`** | DevTools | Web performance, DOM inspection, and console audit | `npx -y @chrome-devtools/mcp-server` |

---

## 🛠️ Ready-to-Use Agent Configuration Blueprints

### Cursor (`.cursorrules`)
Store in your repository root as `.cursorrules`:
```markdown
# Role & Philosophy
You are an expert senior software engineer. Prioritize clean architecture, strict typing, and minimal regressions.

# Coding Guidelines
- Maintain documentation integrity: Never strip existing comments or docstrings.
- Always prefer pure functions and immutable data transformations.
- In TypeScript: Use strict mode, avoid `any`, prefer discriminated unions over enums.
- Always include automated test cases for edge conditions.
```

### Claude Code (`CLAUDE.md`)
Store in your repository root as `CLAUDE.md`:
```markdown
# Project Overview
Production service built with TypeScript & Node.js.

# Commands
- Build: `pnpm build`
- Test: `pnpm test`
- Lint: `pnpm lint --fix`

# Architecture Rules
- Controllers handle HTTP routing; services handle business logic; repositories handle data access.
- All database queries must use prepared statements and connection pooling.
```

### Google Antigravity (`AGENTS.md`)
Store in your repository root as `AGENTS.md`:
```markdown
# Agent Directives
- Prefer interactive sidecar viewers for visualization tasks.
- Keep context lean: Use subagents for broad codebase research and log scraping.
- Verify every modification with unit tests before declaring completion.
```

---

## 📊 Context Window & Token Economics

Managing context windows is critical for agent reliability and cost efficiency:

1. **The 60% Threshold:** Once an agent's context window exceeds 60% capacity, instruction following accuracy begins to degrade exponentially.
2. **Subagent Offloading:** Delegate noisy operations (e.g. searching 50 files or reviewing 1,000 log lines) to short-lived subagents that return only a 3-sentence summary.
3. **Structured Artifacts:** Persist long-term plans and state in markdown artifacts (`task.md`) rather than keeping the entire conversational history in memory.

---

## 🚀 Interactive Setup CLI

Initialize agent rules and MCP configs for your project in seconds:

```bash
# Clone the repository
git clone https://github.com/DYNOSuprovo/awesome-agentic-patterns.git

# Run the setup wizard
python awesome-agentic-patterns/scripts/setup_agent.py
```

The CLI inspects your workspace, detects whether you use Next.js, Python, Node, Go, or Rust, and generates production-ready `.cursorrules`, `CLAUDE.md`, and `mcp.json` automatically!

---

## 🤝 Contributing

Contributions are welcomed! Have a new MCP server, production prompt pattern, or architecture diagram?
1. Fork the repo.
2. Create your feature branch (`git checkout -b feature/new-pattern`).
3. Commit your changes (`git commit -m 'Add Multi-Agent Reflection blueprint'`).
4. Push to the branch (`git push origin feature/new-pattern`).
5. Open a Pull Request.

---

## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.
