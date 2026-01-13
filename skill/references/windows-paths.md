# Windows Path Conversion for Git Bash

## The Problem

Windows uses backslashes and drive letters (e.g., `C:\Program Files\anaconda3`), but Git Bash on Windows uses Unix-style paths with forward slashes (e.g., `/c/Program Files/anaconda3`).

When configuring `.claude/settings.json` for Windows with Git Bash, convert paths to Git Bash format.

## Conversion Rules

### Drive Letters

Convert `C:` to `/c/`, `D:` to `/d/`, etc.

```
C:\Program Files\anaconda3  →  /c/Program Files/anaconda3
D:\workspace\project        →  /d/workspace/project
```

### Path Separators

Replace all backslashes `\` with forward slashes `/`.

```
C:\Users\John\anaconda3  →  /c/Users/John/anaconda3
D:\Program Files\anaconda3\envs\myenv  →  /d/Program Files/anaconda3/envs/myenv
```

### Spaces in Paths

Keep spaces as-is. Git Bash handles spaces correctly without escaping in JSON strings.

```
C:\Program Files\anaconda3  →  /c/Program Files/anaconda3
```

## Common Conda Installation Paths

### Default Installations

| Windows Path | Git Bash Path |
|-------------|---------------|
| `C:\ProgramData\anaconda3` | `/c/ProgramData/anaconda3` |
| `C:\Users\<user>\anaconda3` | `/c/Users/<user>/anaconda3` |
| `D:\Program Files\anaconda3` | `/d/Program Files/anaconda3` |

### Environment Paths

| Windows Path | Git Bash Path |
|-------------|---------------|
| `C:\ProgramData\anaconda3\envs\hrms-algo` | `/c/ProgramData/anaconda3/envs/hrms-algo` |
| `C:\Users\John\anaconda3\envs\dev` | `/c/Users/John/anaconda3/envs/dev` |

## Example Configuration

### Windows with Git Bash

```json
{
  "env": {
    "PATH": "/c/ProgramData/anaconda3/envs/hrms-algo:/c/ProgramData/anaconda3/envs/hrms-algo/Scripts:/c/ProgramData/anaconda3/condabin:${PATH}",
    "CONDA_DEFAULT_ENV": "hrms-algo",
    "CONDA_PREFIX": "/c/ProgramData/anaconda3/envs/hrms-algo"
  }
}
```

### Windows with MinGW64

If using MinGW64 (default in Git for Windows):

```json
{
  "env": {
    "PATH": "C:/ProgramData/anaconda3/envs/hrms-algo: C:/ProgramData/anaconda3/envs/hrms-algo/Scripts:C:/ProgramData/anaconda3/condabin:${PATH}",
    "CONDA_DEFAULT_ENV": "hrms-algo",
    "CONDA_PREFIX": "C:/ProgramData/anaconda3/envs/hrms-algo"
  }
}
```

Note: Some Git Bash versions accept forward slashes with drive letters.

## Verification

After setting up the configuration, verify paths work:

```bash
# Check CONDA_PREFIX
echo $CONDA_PREFIX
# Expected: /c/ProgramData/anaconda3/envs/hrms-algo

# Check which python
which python
# Expected: /c/ProgramData/anaconda3/envs/hrms-algo/python

# Verify Python works
python -c "import sys; print(sys.executable)"
# Expected: /c/ProgramData/anaconda3/envs/hrms-algo/python.exe
```

## Troubleshooting

### Command Not Found

If `which python` shows nothing or wrong path:

1. Verify PATH conversion is correct
2. Check for typos in environment name
3. Ensure conda environment actually exists

### Invalid JSON

If `.claude/settings.json` fails to load:

1. Use forward slashes in paths
2. Escape double quotes in paths if present (rare)
3. Validate JSON with `python -m json.tool .claude/settings.json`

### Path Not Found

If Python can't find modules:

1. Verify PYTHONPATH includes site-packages directory
2. Check that packages are installed in the conda environment
3. Use absolute paths, not relative paths
