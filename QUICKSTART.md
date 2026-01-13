# Quick Start Guide

快速发布此项目到GitHub的步骤。

## 一、创建GitHub仓库

### 方法1：使用GitHub CLI（推荐）

```bash
# 1. 登录GitHub
gh auth login

# 2. 创建仓库并推送
cd /d/workspace/claude-code-conda-env-setup
gh repo create claude-code-conda-env-setup \
  --public \
  --description "Automatic conda environment setup for Claude Code workspaces" \
  --source=. \
  --remote=origin \
  --push
```

### 方法2：手动创建

1. 访问 https://github.com/new
2. 仓库名称：`claude-code-conda-env-setup`
3. 描述：`Automatic conda environment setup for Claude Code workspaces`
4. 选择 Public 或 Private
5. **不要**初始化README（已存在）
6. 点击 "Create repository"

然后执行：

```bash
cd /d/workspace/claude-code-conda-env-setup
git remote add origin https://github.com/你的用户名/claude-code-conda-env-setup.git
git branch -M main
git push -u origin main
```

## 二、创建Release

### 使用GitHub CLI

```bash
cd /d/workspace/claude-code-conda-env-setup
gh release create v1.0.0 \
  --title "v1.0.0 - Initial Release" \
  --notes "Initial release of conda environment setup skill for Claude Code"
```

### 使用Web界面

1. 访问仓库页面
2. 点击右侧 "Releases"
3. 点击 "Create a new release"
4. 填写：
   - Tag: `v1.0.0`
   - Title: `v1.0.0 - Initial Release`
   - Description: 见下文

## 三、Release描述模板

```markdown
## v1.0.0 - Initial Release

### Features
- Automatic conda environment configuration for Claude Code
- Cross-platform support (Windows, Linux, macOS)
- Validation script for configuration verification
- Comprehensive documentation
- Windows Git Bash path conversion guide

### Quick Install
```bash
cd /path/to/workspace
mkdir -p .claude/skills
git clone https://github.com/你的用户名/claude-code-conda-env-setup.git .claude/skills/conda-env-setup
```

### Documentation
- [Installation Guide](https://github.com/你的用户名/claude-code-conda-env-setup/blob/main/docs/installation.md)
- [Skill Documentation](https://github.com/你的用户名/claude-code-conda-env-setup/blob/main/skill/README.md)
```

## 四、添加仓库标签（Topics）

在仓库 Settings → Topics 添加：

- `claude-code`
- `conda`
- `python-environment`
- `development-tools`
- `automation`
- `workspace-configuration`

## 五、更新仓库设置

1. **Description** (Settings → General):
   ```
   Automatic conda environment setup for Claude Code workspaces. Configure Python environments without shell activation.
   ```

2. **License** (Settings → General):
   - 选择 "MIT License"

3. **Website** (可选):
   - 如果有项目主页或文档站点

## 六、验证发布

发布后检查：

- [ ] 代码已推送到GitHub
- [ ] Release页面显示v1.0.0
- [ ] README.md正确显示
-   [ ] LICENSE文件显示
- [ ] 所有文档链接有效

## 七、测试安装

从新安装的仓库测试：

```bash
# 在另一个工作区测试
cd /tmp/test-workspace
mkdir -p .claude/skills
git clone https://github.com/你的用户名/claude-code-conda-env-setup.git .claude/skills/conda-env-setup
python .claude/skills/conda-env-setup/scripts/validate_env.py
```

## 下一步

查看完整文档：
- [发布指南](docs/release-notes.md) - 详细的发布流程
- [安装指南](docs/installation.md) - 用户安装说明
- [贡献指南](CONTRIBUTING.md) - 如何贡献代码

## 常见问题

### Q: 如何修改仓库URL？

```bash
git remote set-url origin https://github.com/新用户名/仓库名.git
```

### Q: 如何删除仓库？

Settings → General → Scroll to bottom → "Delete this repository"

### Q: 如何设置默认分支？

Settings → Branches → Default branch → 选择 `main`

---

**恭喜！** 🎉 您的项目已准备好发布到GitHub。
