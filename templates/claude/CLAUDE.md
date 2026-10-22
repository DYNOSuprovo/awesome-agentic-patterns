# Claude Code Workflow Guide

## 🏗️ Project Architecture
- **Layered Structure**: Follow strict separation of concerns (API Controllers -> Domain Services -> Data Layer).
- **Dependency Flow**: Depend inward toward domain models; high-level business rules should never depend on low-level database drivers.

## ⚡ Build & Test Commands
- **Lint**: Run the project linter and fix errors before committing.
- **Test**: Run test suite (`pytest`, `npm test`, or `cargo test`). Ensure 100% pass rate before requesting review.
- **Build**: Ensure artifacts compile with zero warnings in release mode.

## 🤖 Agent Execution Rules
1. **Explore Before Editing**: Read surrounding code and existing patterns before making modifications.
2. **Atomic Edits**: Avoid broad refactorings across unrelated files in a single session.
3. **Verify Everything**: Always run verification commands (test suite, build check, type checker) after applying edits.
