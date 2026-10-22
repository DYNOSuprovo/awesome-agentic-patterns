# Contributing to Awesome Agentic Patterns

Thank you for your interest in contributing to **Awesome Agentic Patterns**! This repository aims to be the most comprehensive, production-grade guide for AI agents, MCP tooling, and developer workflows.

---

## 🌟 How Can You Contribute?

You can contribute in several ways:
1. **Adding an Architectural Pattern**: Submit a diagram and real-world failure/success analysis of an agent pattern (e.g., Critic-Actor, MapReduce agents, Memory-Augmented loops).
2. **Adding an MCP Server**: Introduce a battle-tested MCP server with connection parameters and configuration snippets.
3. **Adding Rules & Prompt Templates**: Share verified `.cursorrules`, `CLAUDE.md`, or `AGENTS.md` templates tailored for specific frameworks (e.g., Flutter, Rust, PyTorch).
4. **Improving the Setup CLI**: Extend `scripts/setup_agent.py` to auto-detect more project frameworks.

---

## 📋 Contribution Guidelines

### Adding an MCP Server
When submitting an MCP server to the directory:
- Must have an active repository or npm/PyPI package.
- Must include a concise 1-sentence description of permissions/safety implications.
- Must provide the exact CLI launch command (`uvx` or `npx`).

### Adding Agent Rules Templates
When submitting `.cursorrules` or `CLAUDE.md`:
- Focus on actionable constraints rather than generic praise ("Write clean code").
- Include instructions on how the agent should handle edge cases, testing, and file integrity.
- Keep token size reasonable (under 500 tokens per rule file).

---

## 🛠️ Pull Request Process

1. Fork the repo and create your branch from `main`:
   ```bash
   git checkout -b feature/my-new-agent-pattern
   ```
2. Verify linting and syntax:
   ```bash
   python scripts/setup_agent.py --help
   ```
3. Commit your changes using Conventional Commits:
   - `feat: add Anthropic Swarm handoff pattern`
   - `docs: update MCP Postgres server entry`
   - `fix: correct typo in CLAUDE.md template`
4. Push to your fork and submit a Pull Request to `DYNOSuprovo/awesome-agentic-patterns`.
5. Ensure all CI checks pass.

Thank you for making the AI engineering ecosystem better!
