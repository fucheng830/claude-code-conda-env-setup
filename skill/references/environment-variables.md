# Environment Variables for Conda Setup

## Overview

Configure these environment variables in `.claude/settings.json` to make a conda environment available without shell activation.

## Required Variables

### PATH

**Purpose:** Locate executables (python, pip, conda, etc.)

**Format:** Colon-separated list of directories (Unix-style on all platforms)

**Required entries:**
1. `<env_path>` - Conda environment root (contains python.exe)
2. `<env_path>/Scripts` - Windows executables (pip.exe, conda.exe on Windows)
3. `<conda_base>/condabin` - Conda commands (conda.exe on Windows/Linux/macOS)
4. `${PATH}` - Append system PATH

**Windows example:**
```
/c/ProgramData/anaconda3/envs/myenv:/c/ProgramData/anaconda3/envs/myenv/Scripts:/c/ProgramData/anaconda3/condabin:${PATH}
```

**Linux/macOS example:**
```
/home/user/anaconda3/envs/myenv:/home/user/anaconda3/envs/myenv/bin:/home/user/anaconda3/condabin:${PATH}
```

**Why this order:**
- Environment's python/Scripts first (priority)
- condabin for conda commands
- System PATH last (fallback)

### CONDA_DEFAULT_ENV

**Purpose:** Name of the active conda environment

**Value:** Environment name (not path)

**Example:**
```
myenv
hrms-algo
development
```

**Usage:** Some tools check this variable to detect conda environment

### CONDA_PREFIX

**Purpose:** Path to the active conda environment

**Value:** Full path to environment directory

**Windows example (Git Bash):**
```
/c/ProgramData/anaconda3/envs/myenv
```

**Linux/macOS example:**
```
/home/user/anaconda3/envs/myenv
```

**Usage:** Tools use this to find environment directories like `lib`, `include`, etc.

## Optional Variables

### PYTHONPATH

**Purpose:** Additional directories for Python to search for modules

**When needed:** If Python can't find packages in the conda environment

**Format:** Colon-separated list of directories

**Example:**
```
/c/ProgramData/anaconda3/envs/myenv/Lib/site-packages:${PYTHONPATH}
```

**Note:** Most conda setups work without PYTHONPATH. Only add if experiencing import issues.

## Platform-Specific Notes

### Windows

**Binary locations:**
- Python: `<env>/python.exe`
- Scripts: `<env>/Scripts/*.exe`
- Conda: `<conda_base>/condabin/conda.exe`

**Path separator:** Colon (`:`) even on Windows (Git Bash uses Unix-style)

### Linux

**Binary locations:**
- Python: `<env>/bin/python`
- Scripts: `<env>/bin/*`
- Conda: `<conda_base>/condabin/conda` or `<conda_base>/bin/conda`

**Path separator:** Colon (`:`)

### macOS

Same as Linux.

## Complete Examples

### Minimal Configuration (Windows)

```json
{
  "env": {
    "PATH": "/c/ProgramData/anaconda3/envs/myenv:/c/ProgramData/anaconda3/envs/myenv/Scripts:/c/ProgramData/anaconda3/condabin:${PATH}",
    "CONDA_DEFAULT_ENV": "myenv",
    "CONDA_PREFIX": "/c/ProgramData/anaconda3/envs/myenv"
  }
}
```

### Minimal Configuration (Linux/macOS)

```json
{
  "env": {
    "PATH": "/home/user/anaconda3/envs/myenv:/home/user/anaconda3/envs/myenv/bin:/home/user/anaconda3/condabin:${PATH}",
    "CONDA_DEFAULT_ENV": "myenv",
    "CONDA_PREFIX": "/home/user/anaconda3/envs/myenv"
  }
}
```

### With PYTHONPATH (if needed)

```json
{
  "env": {
    "PATH": "/c/ProgramData/anaconda3/envs/myenv:/c/ProgramData/anaconda3/envs/myenv/Scripts:/c/ProgramData/anaconda3/condabin:${PATH}",
    "CONDA_DEFAULT_ENV": "myenv",
    "CONDA_PREFIX": "/c/ProgramData/anaconda3/envs/myenv",
    "PYTHONPATH": "/c/ProgramData/anaconda3/envs/myenv/Lib/site-packages:${PYTHONPATH}"
  }
}
```

## Troubleshooting

### Wrong Python interpreter

**Symptom:** `which python` shows system Python, not conda Python

**Solution:**
1. Verify PATH starts with conda environment path
2. Check for path syntax errors (Windows: use forward slashes)
3. Restart Claude Code to reload configuration

### Packages not found

**Symptom:** `import numpy` fails even though installed

**Solution:**
1. Add PYTHONPATH pointing to environment's site-packages
2. Verify package is installed in correct environment
3. Check CONDA_PREFIX matches environment path

### Conda command not found

**Symptom:** `conda --version` fails

**Solution:**
1. Verify condabin is in PATH
2. Check path to conda installation is correct
3. Ensure conda environment exists: `conda env list`

## Variable Precedence

Claude Code loads environment variables in this order (later overrides earlier):

1. System environment variables
2. Global `~/.claude/settings.json`
3. Workspace `<project>/.claude/settings.json`
4. Local `~/.claude/settings.local.json`

Workspace configuration takes precedence, making it ideal for project-specific conda environments.
