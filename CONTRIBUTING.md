# Contributing to Claude Code Conda Environment Setup Skill

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## How to Contribute

### Reporting Bugs

1. Search existing [issues](https://github.com/yourusername/claude-code-conda-env-setup/issues) to avoid duplicates
2. Create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected behavior
   - Actual behavior
   - Environment details (OS, conda version, Claude Code version)
   - Validation script output if applicable

### Suggesting Enhancements

1. Check existing issues and pull requests
2. Create a feature request with:
   - Clear description of the enhancement
   - Use cases and benefits
   - Possible implementation approach
   - Examples if applicable

### Submitting Pull Requests

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Commit with clear messages
5. Push to your fork
6. Create a pull request

## Development Setup

### 1. Clone Your Fork

```bash
git clone https://github.com/yourusername/claude-code-conda-env-setup.git
cd claude-code-conda-env-setup
```

### 2. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

### 3. Make Changes

Edit files in the `skill/` directory:

- `SKILL.md` - Skill definition and behavior
- `scripts/` - Utility scripts
- `references/` - Documentation
- `examples/` - Example configurations

### 4. Test Your Changes

**Test the skill:**

1. Copy to a test workspace:
   ```bash
   cp -r skill /path/to/test/workspace/.claude/skills/conda-env-setup
   ```

2. Restart Claude Code

3. Test skill activation and functionality

**Test validation script:**

```bash
python skill/scripts/validate_env.py
```

**Validate documentation:**

- Check for broken links
- Verify code examples work
- Test on multiple platforms if possible

### 5. Commit Changes

Use clear, descriptive commit messages:

```bash
git add .
git commit -m "Add: Feature description"
# or
git commit -m "Fix: Bug fix description"
# or
git commit -m "Docs: Documentation update description"
```

Commit message prefixes:
- `Add:` - New features
- `Fix:` - Bug fixes
- `Docs:` - Documentation changes
- `Refactor:` - Code refactoring
- `Test:` - Adding or updating tests
- `Chore:` - Maintenance tasks

### 6. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a pull request on GitHub with:
- Clear title
- Description of changes
- Reference related issues
- Screenshots if applicable

## Coding Standards

### Python Scripts

- Follow PEP 8 style guide
- Use type hints where appropriate
- Add docstrings to functions
- Include error handling

Example:
```python
def validate_config(config_path: str) -> bool:
    """Validate the configuration file.

    Args:
        config_path: Path to the configuration file

    Returns:
        True if valid, False otherwise
    """
    try:
        with open(config_path) as f:
            json.load(f)
        return True
    except (JSONDecodeError, FileNotFoundError):
        return False
```

### Documentation

- Use clear, concise language
- Include examples for complex topics
- Use imperative mood
- Add platform-specific notes when relevant

### SKILL.md

- Use third-person in description
- Include specific trigger phrases
- Keep body lean (1500-2000 words)
- Move detailed content to references/

## Project Structure

```
claude-code-conda-env-setup/
├── skill/                    # Core skill files
│   ├── SKILL.md             # Main skill definition
│   ├── scripts/             # Utility scripts
│   ├── references/          # Documentation
│   └── examples/            # Examples
├── docs/                    # Additional docs
├── README.md                # Project readme
├── CONTRIBUTING.md          # This file
├── LICENSE                  # MIT License
└── .gitignore              # Git ignore rules
```

## Testing

### Manual Testing Checklist

Before submitting a PR, test:

- [ ] Skill activates on trigger phrases
- [ ] Validation script runs without errors
- [ ] Documentation is clear and accurate
- [ ] Code examples work as documented
- [ ] No broken links in documentation
- [ ] Works on target platforms (Windows/Linux/macOS)

### Platform Testing

Test on your target platform(s):

**Windows:**
- Git Bash paths work correctly
- Forward slashes in paths
- JSON escaping for spaces

**Linux/macOS:**
- Standard Unix paths
- Proper permissions on scripts

## Documentation Updates

When changing functionality:

1. Update SKILL.md if behavior changes
2. Update relevant files in `references/`
3. Add new examples to `examples/`
4. Update README.md if needed
5. Update installation guide if workflow changes

## Release Process

Maintainers follow this process for releases:

1. Update version in SKILL.md
2. Update CHANGELOG.md
3. Create git tag: `git tag v1.x.x`
4. Push tag: `git push origin v1.x.x`
5. Create GitHub release

## Style Guidelines

### Writing Style

- Use imperative mood: "Create a file" not "You should create a file"
- Be concise and direct
- Use active voice
- Avoid jargon when possible

### Code Comments

- Explain why, not what
- Keep comments up-to-date
- Use clear, simple language

## Questions?

If you have questions:

1. Check existing issues and discussions
2. Review the documentation
3. Create an issue with the "question" label

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Code of Conduct

Be respectful, inclusive, and professional. We welcome contributors from all backgrounds and experience levels.

## Recognition

Contributors will be recognized in the project's CONTRIBUTORS.md file.

Thank you for contributing!
