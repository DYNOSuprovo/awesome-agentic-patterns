#!/usr/bin/env python3
"""
Awesome Agentic Patterns - Project Setup CLI
Inspects your workspace, detects your project stack, and generates tailored
AI agent configuration rules (.cursorrules, CLAUDE.md, AGENTS.md, mcp.json).
"""

import os
import sys
import argparse
import shutil
from pathlib import Path

TEMPLATES = {
    "cursor": Path(__file__).resolve().parent.parent / "templates" / "cursor" / ".cursorrules",
    "claude": Path(__file__).resolve().parent.parent / "templates" / "claude" / "CLAUDE.md",
    "antigravity": Path(__file__).resolve().parent.parent / "templates" / "antigravity" / "AGENTS.md",
    "mcp": Path(__file__).resolve().parent.parent / "templates" / "mcp" / "mcp_config.json",
}

def detect_stack(target_dir: Path) -> dict:
    features = {
        "python": (target_dir / "pyproject.toml").exists() or (target_dir / "requirements.txt").exists() or (target_dir / "setup.py").exists(),
        "node_ts": (target_dir / "package.json").exists() or (target_dir / "tsconfig.json").exists(),
        "go": (target_dir / "go.mod").exists(),
        "rust": (target_dir / "Cargo.toml").exists(),
        "git": (target_dir / ".git").is_dir(),
    }
    return features

def banner():
    print("=" * 60)
    print("[*] Awesome Agentic Patterns - Workspace Setup CLI")
    print("=" * 60)

def main():
    parser = argparse.ArgumentParser(description="Configure production agent rules for your workspace.")
    parser.add_argument("--target", "-t", default=".", help="Target workspace directory (default: current directory)")
    parser.add_argument("--all", "-a", action="store_true", help="Generate all agent rule files (.cursorrules, CLAUDE.md, AGENTS.md, mcp.json)")
    parser.add_argument("--force", "-f", action="store_true", help="Overwrite existing configuration files")
    parser.add_argument("--dry-run", action="store_true", help="Simulate generation without writing files")

    args = parser.parse_args()
    target_path = Path(args.target).resolve()

    banner()
    print(f"[*] Scanning workspace: {target_path}")

    if not target_path.exists():
        print(f"[!] Error: Target directory does not exist: {target_path}")
        sys.exit(1)

    stack = detect_stack(target_path)
    detected = [k for k, v in stack.items() if v]
    print(f"[*] Detected Technologies: {', '.join(detected) if detected else 'Generic / Polyglot'}")

    configs_to_install = [
        ("Cursor Rules", TEMPLATES["cursor"], target_path / ".cursorrules"),
        ("Claude Code Rules", TEMPLATES["claude"], target_path / "CLAUDE.md"),
        ("Antigravity Agents Guide", TEMPLATES["antigravity"], target_path / "AGENTS.md"),
        ("MCP Server Config", TEMPLATES["mcp"], target_path / "mcp.json"),
    ]

    for label, src_file, dst_file in configs_to_install:
        if dst_file.exists() and not args.force:
            print(f"[-] Skipped {label}: {dst_file.name} already exists (use --force to overwrite)")
            continue

        if args.dry_run:
            print(f"[DRY RUN] Would create {label} at {dst_file}")
        else:
            if src_file.exists():
                shutil.copyfile(src_file, dst_file)
                print(f"[+] Installed {label} -> {dst_file.name}")
            else:
                print(f"[!] Template source missing: {src_file}")

    print("\n[OK] Workspace setup complete! You are ready to pair with production AI agents.")

if __name__ == "__main__":
    main()
