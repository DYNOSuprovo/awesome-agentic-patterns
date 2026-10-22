# Antigravity Agent Configuration Guide

## 🎯 Strategic Directives
- **Sidecar Preference**: For scientific, biomolecular, or UI visualizations, always prioritize interactive sidecar viewers over static image generation or raw text summaries.
- **Context Management**: When analyzing massive codebases or scanning logs, invoke specialized research subagents to keep the primary orchestrator's context window lean.
- **Verification First**: Never report a task as complete without running automated tests or lint verification tools to confirm zero regressions.

## 👥 Subagent Delegation Matrix
| Subagent Role | Purpose | Permitted Tools |
| :--- | :--- | :--- |
| `research` | Codebase exploration, web searches, documentation lookups | Read-only tools |
| `coding` | Implementation, refactoring, unit test authoring | Read, Write, Command execution |
| `reviewer` | Architectural and security review of proposed diffs | Read-only tools |
