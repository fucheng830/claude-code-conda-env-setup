# Creating GitHub Release

Follow these steps to create a GitHub release for this project.

## Prerequisites

1. All changes committed and pushed to GitHub
2. Repository created on GitHub
3. Git remote configured

## Step 1: Create GitHub Repository

### Option A: Using GitHub CLI

```bash
# Install gh CLI if needed
# https://cli.github.com/

# Login to GitHub
gh auth login

# Create repository
gh repo create claude-code-conda-env-setup \
  --public \
  --description "Automatic conda environment setup for Claude Code workspaces" \
  --source=. \
  --remote=origin \
  --push
```

### Option B: Manual Creation

1. Go to https://github.com/new
2. Repository name: `claude-code-conda-env-setup`
3. Description: `Automatic conda environment setup for Claude Code workspaces`
4. Choose Public or Private
5. Don't initialize with README (already exists)
6. Click "Create repository"

Then add remote and push:

```bash
cd /d/workspace/claude-code-conda-env-setup
git remote add origin https://github.com/yourusername/claude-code-conda-env-setup.git
git branch -M main
git push -u origin main
```

## Step 2: Create Release on GitHub

### Using GitHub Web UI

1. Go to repository on GitHub
2. Click "Releases" in the right sidebar
3. Click "Create a new release"
4. Fill in:
   - **Tag version**: `v1.0.0`
   - **Target**: `main`
   - **Release title**: `v1.0.0 - Initial Release`
   - **Description**: (use content below)

### Using GitHub CLI

```bash
gh release create v1.0.0 \
  --title "v1.0.0 - Initial Release" \
  --notes "See release notes below"
```

## Release Notes Template

### v1.0.0 - Initial Release

#### Features

- Automatic conda environment configuration for Claude Code workspaces
- Cross-platform support (Windows, Linux, macOS)
- Validation script for configuration verification
- Comprehensive documentation with examples
- Windows Git Bash path conversion guide
- Environment variables reference documentation

#### Installation

Quick install:
```bash
cd /path/to/workspace
mkdir -p .claude/skills
git clone https://github.com/yourusername/claude-code-conda-env-setup.git .claude/skills/conda-env-setup
```

#### Documentation

- [README](https://github.com/yourusername/claude-code-conda-env-setup/blob/main/README.md)
- [Installation Guide](https://github.com/yourusername/claude-code-conda-env-setup/blob/main/docs/installation.md)
- [Skill Documentation](https://github.com/yourusername/claude-code-conda-env-setup/blob/main/skill/README.md)

#### Usage

The skill automatically activates when you ask Claude to:
- "setup conda environment"
- "configure Python environment"
- "activate conda automatically"
- "set conda environment for workspace"

#### Known Issues

None at this time

#### Contributors

- Initial development

## Step 3: Add Topics/Tags

Add repository topics for discoverability:

1. Go to repository Settings
2. Scroll to "Topics"
3. Add topics:
   - `claude-code`
   - `conda`
   - `python-environment`
   - `development-tools`
   - `skill`
   - `automation`
   - `workspace-configuration`

## Step 4: Add Repository Description

Update repository description (Settings → General):

```
Automatic conda environment setup for Claude Code workspaces. Configure Python environments without shell activation using environment variables.
```

## Step 5: Create LICENSE Display

Ensure the LICENSE file is displayed:
- Go to Settings → General
- Scroll to "License"
- Select "MIT License"

## Step 6: Setup Branch Protection (Recommended)

1. Go to Settings → Branches
2. Add rule for `main` branch:
   - ✓ Require pull request reviews before merging
   - ✓ Require status checks to pass before merging
   - ✓ Require branches to be up to date before merging

## Step 7: Add badges to README.md

Add these badges to the top of README.md:

```markdown
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub release](https://img.shields.io/github/v/release/yourusername/claude-code-conda-env-setup)](https://github.com/yourusername/claude-code-conda-env-setup/releases)
```

## Post-Release Checklist

- [ ] Release created on GitHub
- [ ] Tag pushed to repository
- [ ] Documentation links work
- [ ] Topics added
- [ ] Repository description set
- [ ] License displayed correctly
- [ ] Badges added to README
- [ ] Branch protection rules set (optional)

## Announcing the Release

Consider announcing the release:

1. **Claude Code Community**: Post in relevant forums
2. **Social Media**: Share on Twitter, LinkedIn, etc.
3. **Blog**: Write a blog post if you have one
4. **Reddit**: Post to relevant subreddits

Example announcement:

```
🎉 Excited to announce v1.0.0 of claude-code-conda-env-setup!

A skill for Claude Code that automatically configures conda environments
without requiring shell activation.

Features:
✅ Cross-platform (Windows/Linux/macOS)
✅ Validation script included
✅ Comprehensive documentation
✅ Zero configuration after installation

Get started: https://github.com/yourusername/claude-code-conda-env-setup

#ClaudeCode #Conda #Python
```

## Maintenance

### Release Process for Future Versions

1. Update version in `skill/SKILL.md`
2. Update CHANGELOG.md (create this file)
3. Commit changes
4. Create git tag:
   ```bash
   git tag v1.x.x
   git push origin v1.x.x
   ```
5. Create GitHub release
6. Update badges in README

### Backward Compatibility

- Follow semantic versioning
- Document breaking changes clearly
- Provide migration guides for major versions

## Support

After release:
- Monitor Issues section
- Respond to questions and bug reports
- Review and merge pull requests
- Update documentation as needed

---

Congratulations on your release! 🎉
