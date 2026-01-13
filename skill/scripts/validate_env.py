#!/usr/bin/env python3
"""Validate conda environment configuration for Claude Code workspace.

This script checks if the workspace's .claude/settings.json is properly
configured for a conda environment.
"""
import json
import os
import sys
from pathlib import Path


def check_env_var(name, expected_contains=None):
    """Check if environment variable is set."""
    value = os.environ.get(name)
    if value:
        status = "OK"
        if expected_contains and expected_contains in value:
            status = f"OK (contains '{expected_contains}')"
        return True, status, value
    return False, "MISSING", None


def validate_config():
    """Validate the conda environment configuration."""
    print("=" * 60)
    print("Conda Environment Configuration Validation")
    print("=" * 60)
    print()

    all_passed = True

    # Check environment variables
    print("1. Environment Variables")
    print("-" * 60)

    checks = [
        ("CONDA_DEFAULT_ENV", None, "Conda environment name"),
        ("CONDA_PREFIX", None, "Conda environment path"),
        ("PATH", None, "Executable search path"),
    ]

    for var_name, expected, description in checks:
        passed, status, value = check_env_var(var_name, expected)
        symbol = "[OK]" if passed else "[FAIL]"
        print(f"{symbol} {var_name:20} - {status}")
        if passed and value and var_name in ["CONDA_DEFAULT_ENV", "CONDA_PREFIX"]:
            print(f"{'':20}   {value}")
        if not passed:
            all_passed = False
        print()

    # Check Python interpreter
    print("2. Python Interpreter")
    print("-" * 60)

    python_path = sys.executable
    if python_path:
        conda_prefix = os.environ.get("CONDA_PREFIX", "")
        if conda_prefix and conda_prefix.replace("\\", "/") in python_path.replace("\\", "/"):
            print(f"[OK] Python is in configured conda environment")
            print(f"{'':4}Path: {python_path}")
        else:
            print(f"[WARN] Python may not be in configured conda environment")
            print(f"{'':4}Path: {python_path}")
            print(f"{'':4}Expected prefix: {conda_prefix}")
        print()
    else:
        print(f"[FAIL] Python interpreter not found")
        all_passed = False
        print()

    # Check .claude/settings.json
    print("3. Workspace Configuration")
    print("-" * 60)

    workspace_settings = Path.cwd() / ".claude" / "settings.json"
    if workspace_settings.exists():
        print(f"[OK] Workspace settings found: {workspace_settings}")
        try:
            with open(workspace_settings) as f:
                config = json.load(f)
            env_config = config.get("env", {})
            if env_config:
                print(f"[OK] Environment configuration defined")
                for key in ["PATH", "CONDA_DEFAULT_ENV", "CONDA_PREFIX"]:
                    if key in env_config:
                        print(f"{'':4}{key}: {env_config[key][:50]}{'...' if len(env_config[key]) > 50 else ''}")
            else:
                print(f"[WARN] No 'env' section in settings.json")
                all_passed = False
        except json.JSONDecodeError as e:
            print(f"[FAIL] Invalid JSON in settings.json: {e}")
            all_passed = False
        except Exception as e:
            print(f"[FAIL] Error reading settings.json: {e}")
            all_passed = False
    else:
        print(f"[FAIL] Workspace settings not found: {workspace_settings}")
        all_passed = False
    print()

    # Summary
    print("=" * 60)
    if all_passed:
        print("RESULT: All checks PASSED")
        print()
        print("Your conda environment is properly configured.")
        print("Python commands will use the configured environment.")
    else:
        print("RESULT: Some checks FAILED")
        print()
        print("Please review the failed checks above and update")
        print(".claude/settings.json to configure your conda environment.")
    print("=" * 60)

    return all_passed


if __name__ == "__main__":
    success = validate_config()
    sys.exit(0 if success else 1)
