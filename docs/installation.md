# Installation Guide

Detailed step-by-step installation instructions for the Conda Environment Setup Skill.

## Prerequisites

Before installing this skill, ensure you have:

1. **Claude Code** installed and working
2. **Conda** installed (Anaconda, Miniconda, or Miniforge)
3. **Git** (for cloning the repository)

Verify your setup:

```bash
# Check Claude Code
claude --version

# Check conda
conda --version

# Check git
git --version
```

## Installation Methods

### Method 1: Clone to Workspace (Recommended)

Install the skill directly into a specific workspace.

#### Step 1: Navigate to Your Workspace

```bash
cd /path/to/your/workspace
```

#### Step 2: Create Skills Directory

```bash
mkdir -p .claude/skills
```

#### Step 3: Clone the Repository

```bash
git clone https://github.com/yourusername/claude-code-conda-env-setup.git .claude/skills/conda-env-setup
```

#### Step 4: Verify Installation

```bash
ls -la .claude/skills/conda-env-setup/
```

Expected output:
```
SKILL.md
README.md
scripts/
references/
examples/
```

### Method 2: Manual Installation

Download and manually install the skill files.

#### Step 1: Download the Repository

Download the ZIP file from GitHub:
```
https://github.com/yourusername/claude-code-conda-env-setup/archive/refs/heads/main.zip
```

#### Step 2: Extract to Workspace

```bash
unzip claude-code-conda-env-setup-main.zip
mv claude-code-conda-env-setup-main/skill .claude/skills/conda-env-setup
rm -rf claude-code-conda-env-setup-main.zip claude-code-conda-env-setup-main
```

#### Step 3: Verify Installation

```bash
ls -la .claude/skills/conda-env-setup/
```

### Method 3: Global Installation (Advanced)

Install for all workspaces using Claude Code's plugin system.

#### Step 1: Locate Claude Code Plugins Directory

```bash
# On Linux/macOS
echo ~/.claude/plugins/

# On Windows
echo ~/.claude/plugins/
```

#### Step 2: Create Plugin Structure

```bash
mkdir -p ~/.claude/plugins/conda-env-setup/skills/conda-env-setup
```

#### Step 3: Copy Skill Files

```bash
cp -r /path/to/claude-code-conda-env-setup/skill/* ~/.claude/plugins/conda-env-setup/skills/conda-env-setup/
```

#### Step 4: Create Plugin Metadata

Create `~/.claude/plugins/conda-env-setup/.claude-plugin/plugin.json`:

```json
{
  "name": "conda-env-setup",
  "version": "1.0.0",
  "description": "Conda environment setup skill for Claude Code",
  "author": "Your Name",
  "license": "MIT"
}
```

## Post-Installation

### 1. Configure Your Conda Environment

After installing the skill, configure your workspace to use a conda environment.

#### Find Your Conda Environment

```bash
# List all conda environments
conda env list

# Find specific environment path
conda env list | grep "your_env_name"
```

#### Create Workspace Configuration

Create `.claude/settings.json` in your workspace root.

**Windows (Git Bash):**
```json
{
  "env": {
    "PATH": "/c/ProgramData/anaconda3/envs/your_env:/c/ProgramData/anaconda3/envs/your_env/Scripts:/c/ProgramData/anaconda3/condabin:${PATH}",
    "CONDA_DEFAULT_ENV": "your_env",
    "CONDA_PREFIX": "/c/ProgramData/anaconda3/envs/your_env"
  }
}
```

**Linux/macOS:**
```json
{
  "env": {
    "PATH": "/home/user/anaconda3/envs/your_env:/home/user/anaconda3/envs/your_env/bin:/home/user/anaconda3/condabin:${PATH}",
    "CONDA_DEFAULT_ENV": "your_env",
    "CONDA_PREFIX": "/home/user/anaconda3/envs/your_env"
  }
}
```

### 2. Validate Installation

Run the validation script to verify everything is working:

```bash
python .claude/skills/conda-env-setup/scripts/validate_env.py
```

Expected output:
```
============================================================
Conda Environment Configuration Validation
============================================================

1. Environment Variables
------------------------------------------------------------
[OK] CONDA_DEFAULT_ENV    - OK
[OK] CONDA_PREFIX         - OK
[OK] PATH                 - OK

2. Python Interpreter
------------------------------------------------------------
[OK] Python is in configured conda environment

3. Workspace Configuration
------------------------------------------------------------
[OK] Workspace settings found
[OK] Environment configuration defined

============================================================
RESULT: All checks PASSED
============================================================
```

### 3. Test the Skill

Restart Claude Code and test the skill:

```
You: "Help me setup conda environment for this workspace"
```

The skill should activate and provide guidance.

## Troubleshooting

### Skill Not Activating

**Problem:** Skill doesn't activate when mentioned

**Solutions:**
1. Verify SKILL.md exists in `.claude/skills/conda-env-setup/`
2. Check that YAML frontmatter is valid
3. Restart Claude Code completely
4. Check for syntax errors in SKILL.md

### Validation Script Fails

**Problem:** Validation shows errors

**Solutions:**
1. Verify `.claude/settings.json` exists and is valid JSON
2. Check that paths use correct format (Windows: forward slashes)
3. Ensure conda environment exists: `conda env list`
4. Verify Python is in the environment

### Wrong Python Interpreter

**Problem:** `which python` shows system Python

**Solutions:**
1. Check PATH order in `.claude/settings.json`
2. Verify CONDA_PREFIX is set correctly
3. Restart Claude Code to reload configuration
4. Run validation script for diagnostics

### Path Issues on Windows

**Problem:** Paths not working on Windows

**Solutions:**
1. Use Git Bash format: `/c/ProgramData` not `C:\ProgramData`
2. Use forward slashes only
3. Quote paths with spaces in JSON
4. Reference: [Windows Path Guide](../skill/references/windows-paths.md)

## Updating the Skill

### Method 1: Git Pull

```bash
cd .claude/skills/conda-env-setup
git pull origin main
```

### Method 2: Re-download

```bash
rm -rf .claude/skills/conda-env-setup
git clone https://github.com/yourusername/claude-code-conda-env-setup.git .claude/skills/conda-env-setup
```

## Uninstallation

### Remove from Workspace

```bash
rm -rf .claude/skills/conda-env-setup
```

### Remove Global Plugin

```bash
rm -rf ~/.claude/plugins/conda-env-setup
```

### Clean Configuration

Remove conda environment configuration from `.claude/settings.json`:

```json
{
  "env": {
    // Remove CONDA_DEFAULT_ENV, CONDA_PREFIX, PATH entries
  }
}
```

## Next Steps

After installation:

1. Read the [Skill Documentation](../skill/README.md)
2. Check [Platform-Specific Guides](../skill/references/)
3. Review [Example Configurations](../skill/examples/)
4. Run the validation script

## Additional Resources

- [Project README](../README.md)
- [Skill Documentation](../skill/README.md)
- [Environment Variables Reference](../skill/references/environment-variables.md)
- [Windows Path Guide](../skill/references/windows-paths.md)
- [Report Issues](https://github.com/yourusername/claude-code-conda-env-setup/issues)

## Getting Help

If you encounter issues:

1. Check the [Troubleshooting](#troubleshooting) section
2. Run the validation script
3. Search existing [GitHub Issues](https://github.com/yourusername/claude-code-conda-env-setup/issues)
4. Create a new issue with:
   - Your operating system and version
   - Conda version (`conda --version`)
   - Claude Code version
   - Output of validation script
   - Content of `.claude/settings.json` (redact sensitive info)
