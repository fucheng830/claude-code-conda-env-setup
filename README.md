# Claude Code - Conda Environment Setup Skill

Automatically configure conda environments for Claude Code workspaces using environment variables instead of shell activation.

## Overview

This skill solves the problem of conda environment activation in Claude Code's bash sessions. Since each bash command runs in a new, non-interactive shell, standard `conda activate` doesn't work. This skill provides an alternative approach using workspace-level environment variables to make Python interpreters and packages available without shell activation.

## Features

- **No Shell Activation Required**: Works via environment variables instead of `conda activate`
- **Cross-Platform**: Supports Windows (Git Bash), Linux, and macOS
- **Automatic Configuration**: Guided setup for workspace-specific conda environments
- **Validation Script**: Built-in validation to verify configuration
- **Comprehensive Documentation**: Detailed guides for paths and environment variables

## Installation

### Option 1: Clone to Workspace `.claude/skills`

Clone this repository into your workspace's `.claude/skills` directory:

```bash
cd /path/to/your/workspace
mkdir -p .claude/skills
git clone https://github.com/yourusername/claude-code-conda-env-setup.git .claude/skills/conda-env-setup
```

### Option 2: Manual Installation

Copy the `skill/` directory to your workspace:

```bash
mkdir -p .claude/skills
cp -r /path/to/claude-code-conda-env-setup/skill .claude/skills/conda-env-setup
```

## Usage

Once installed, the skill automatically activates when you ask Claude to:

- "setup conda environment"
- "configure Python environment"
- "activate conda automatically"
- "set conda environment for workspace"

### Example Workflow

1. **User request**: "Help me setup conda environment for this workspace"

2. **Skill activates** and provides guidance for:
   - Detecting conda installation path
   - Creating/updating `.claude/settings.json`
   - Verifying configuration

3. **Configuration created** in `.claude/settings.json`:

```json
{
  "env": {
    "PATH": "/c/ProgramData/anaconda3/envs/myenv:/c/ProgramData/anaconda3/envs/myenv/Scripts:/c/ProgramData/anaconda3/condabin:${PATH}",
    "CONDA_DEFAULT_ENV": "myenv",
    "CONDA_PREFIX": "/c/ProgramData/anaconda3/envs/myenv"
  }
}
```

4. **Validate** the setup:

```bash
python .claude/skills/conda-env-setup/scripts/validate_env.py
```

## Quick Start

### 1. Identify Your Conda Environment

Find your conda installation and environment:

```bash
# Locate conda
which conda

# List environments
conda env list

# Find environment path
conda env list | grep "env_name"
```

### 2. Create Workspace Configuration

Create or update `.claude/settings.json` in your workspace root:

**Windows (Git Bash):**
```json
{
  "env": {
    "PATH": "/c/ProgramData/anaconda3/envs/myenv:/c/ProgramData/anaconda3/envs/myenv/Scripts:/c/ProgramData/anaconda3/condabin:${PATH}",
    "CONDA_DEFAULT_ENV": "myenv",
    "CONDA_PREFIX": "/c/ProgramData/anaconda3/envs/myenv"
  }
}
```

**Linux/macOS:**
```json
{
  "env": {
    "PATH": "/home/user/anaconda3/envs/myenv:/home/user/anaconda3/envs/myenv/bin:/home/user/anaconda3/condabin:${PATH}",
    "CONDA_DEFAULT_ENV": "myenv",
    "CONDA_PREFIX": "/home/user/anaconda3/envs/myenv"
  }
}
```

### 3. Verify Configuration

```bash
# Check environment variables
echo $CONDA_DEFAULT_ENV
echo $CONDA_PREFIX

# Verify Python interpreter
which python
python -c "import sys; print(sys.executable)"

# Run validation script
python .claude/skills/conda-env-setup/scripts/validate_env.py
```

## Project Structure

```
claude-code-conda-env-setup/
├── README.md                    # This file
├── LICENSE                      # MIT License
├── .gitignore                   # Git ignore rules
├── skill/                       # Skill files
│   ├── SKILL.md                 # Main skill definition
│   ├── README.md                # Skill documentation
│   ├── scripts/                 # Utility scripts
│   │   └── validate_env.py      # Configuration validator
│   ├── references/              # Detailed documentation
│   │   ├── windows-paths.md     # Windows path conversion guide
│   │   └── environment-variables.md  # Env var reference
│   └── examples/                # Example configurations
│       └── example-config.json  # Example .claude/settings.json
└── docs/                        # Additional documentation
    └── installation.md          # Detailed installation guide
```

## Documentation

- **[Skill Documentation](skill/README.md)** - Complete skill guide
- **[Windows Path Guide](skill/references/windows-paths.md)** - Converting Windows paths for Git Bash
- **[Environment Variables Reference](skill/references/environment-variables.md)** - Detailed env var configuration
- **[Installation Guide](docs/installation.md)** - Step-by-step installation instructions

## How It Works

### The Problem

Conda environments cannot be activated through standard `conda activate` in Claude Code's bash sessions because each command runs in a new, non-interactive shell.

### The Solution

Configure the workspace's `.claude/settings.json` to prioritize the conda environment's paths in the `PATH` environment variable. This works because:

1. Shell commands look up executables using PATH
2. First match in PATH gets used
3. No shell initialization required

### Benefits

- No shell initialization needed
- Works across platforms
- Persistent across commands
- No subprocess overhead
- Compatible with all Claude Code features

## Validation Script

The included `validate_env.py` script checks:

- Environment variables (CONDA_DEFAULT_ENV, CONDA_PREFIX, PATH)
- Python interpreter location
- Workspace configuration file
- Overall setup status

Run it anytime to verify your configuration:

```bash
python .claude/skills/conda-env-setup/scripts/validate_env.py
```

## Platform-Specific Notes

### Windows

- Use Git Bash format: `/c/ProgramData/anaconda3` instead of `C:\ProgramData\anaconda3`
- Forward slashes only, no backslashes
- Include `/Scripts` directory for Windows executables

### Linux/macOS

- Standard Unix paths
- Include `/bin` directory for executables

## Troubleshooting

### Python Not Found in Environment

1. Verify PATH entries are correct
2. Check for path syntax errors
3. Ensure `.claude/settings.json` is valid JSON
4. Restart Claude Code

### Packages Not Found

1. Verify PYTHONPATH includes the environment's site-packages
2. Check packages are installed in the conda environment
3. Run validation script

### Configuration Not Applied

1. Confirm `.claude/settings.json` is in workspace root
2. Validate JSON syntax
3. Check for conflicting global settings
4. Restart Claude Code

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Created for Claude Code users working with conda environments
- Inspired by the need for reliable Python environment configuration in AI-assisted development

## Support

For issues, questions, or suggestions, please:
- Open an issue on GitHub
- Check the [documentation](skill/README.md)
- Run the validation script for diagnostics

## Related Projects

- [Claude Code](https://github.com/anthropics/claude-code) - Official Claude Code repository
- [Conda](https://docs.conda.io/) - Conda documentation

---

**Note**: This skill is designed for Claude Code. Make sure you have Claude Code installed before using this skill.
