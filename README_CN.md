# Claude Code - Conda 环境自动配置 Skill

**[English](README.md) | [中文文档](README_CN.md)**

自动为 Claude Code 工作区配置 conda 环境，使用环境变量而非 shell 激活方式。

## 项目简介

本项目解决了在 Claude Code 的 bash 会话中激活 conda 环境的问题。由于每个 bash 命令都在新的非交互式 shell 中运行，标准的 `conda activate` 命令无法正常工作。本项目提供了一种替代方案，通过工作区级别的环境变量配置，使 Python 解释器和包可用，无需 shell 激活。

## 功能特性

- **无需 Shell 激活**：通过环境变量配置，无需使用 `conda activate`
- **跨平台支持**：支持 Windows (Git Bash)、Linux 和 macOS
- **自动配置**：为特定工作区的 conda 环境提供配置指导
- **内置验证**：包含验证脚本来检查配置是否正确
- **完善文档**：提供详细的路径和环境变量指南

## 安装

### 方法1：克隆到工作区的 `.claude/skills`

将此仓库克隆到工作区的 `.claude/skills` 目录：

```bash
cd /path/to/your/workspace
mkdir -p .claude/skills
git clone https://github.com/fucheng830/claude-code-conda-env-setup.git .claude/skills/conda-env-setup
```

### 方法2：手动安装

将 `skill/` 目录复制到您的工作区：

```bash
mkdir -p .claude/skills
cp -r /path/to/claude-code-conda-env-setup/skill .claude/skills/conda-env-setup
```

## 使用方法

安装完成后，当您向 Claude 提出以下请求时，skill 会自动激活：

- "setup conda environment"（配置 conda 环境）
- "configure Python environment"（配置 Python 环境）
- "activate conda automatically"（自动激活 conda）
- "set conda environment for workspace"（为工作区设置 conda 环境）

### 使用示例

1. **用户请求**："帮我为这个工作区配置 conda 环境"

2. **Skill 激活**并提供以下指导：
   - 检测 conda 安装路径
   - 创建/更新 `.claude/settings.json`
   - 验证配置

3. **在工作区根目录创建配置** `.claude/settings.json`：

```json
{
  "env": {
    "PATH": "/c/ProgramData/anaconda3/envs/myenv:/c/ProgramData/anaconda3/envs/myenv/Scripts:/c/ProgramData/anaconda3/condabin:${PATH}",
    "CONDA_DEFAULT_ENV": "myenv",
    "CONDA_PREFIX": "/c/ProgramData/anaconda3/envs/myenv"
  }
}
```

4. **验证配置**：

```bash
python .claude/skills/conda-env-setup/scripts/validate_env.py
```

## 快速开始

### 1. 确认您的 Conda 环境

找到您的 conda 安装和环境：

```bash
# 定位 conda
which conda

# 列出所有环境
conda env list

# 查找环境路径
conda env list | grep "env_name"
```

### 2. 创建工作区配置

在工作区根目录创建或更新 `.claude/settings.json`：

**Windows (Git Bash) 格式：**
```json
{
  "env": {
    "PATH": "/c/ProgramData/anaconda3/envs/myenv:/c/ProgramData/anaconda3/envs/myenv/Scripts:/c/ProgramData/anaconda3/condabin:${PATH}",
    "CONDA_DEFAULT_ENV": "myenv",
    "CONDA_PREFIX": "/c/ProgramData/anaconda3/envs/myenv"
  }
}
```

**Linux/macOS 格式：**
```json
{
  "env": {
    "PATH": "/home/user/anaconda3/envs/myenv:/home/user/anaconda3/envs/myenv/bin:/home/user/anaconda3/condabin:${PATH}",
    "CONDA_DEFAULT_ENV": "myenv",
    "CONDA_PREFIX": "/home/user/anaconda3/envs/myenv"
  }
}
```

### 3. 验证配置

```bash
# 检查环境变量
echo $CONDA_DEFAULT_ENV
echo $CONDA_PREFIX

# 验证 Python 解释器
which python
python -c "import sys; print(sys.executable)"

# 运行验证脚本
python .claude/skills/conda-env-setup/scripts/validate_env.py
```

## 项目结构

```
claude-code-conda-env-setup/
├── README.md                    # 英文项目说明
├── README_CN.md                 # 中文项目说明（本文件）
├── LICENSE                      # MIT 开源协议
├── .gitignore                   # Git 忽略规则
├── skill/                       # Skill 文件
│   ├── SKILL.md                 # Skill 主定义
│   ├── README.md                # Skill 文档
│   ├── scripts/                 # 工具脚本
│   │   └── validate_env.py      # 配置验证器
│   ├── references/              # 详细文档
│   │   ├── windows-paths.md     # Windows 路径转换指南
│   │   └── environment-variables.md  # 环境变量参考
│   └── examples/                # 示例配置
│       └── example-config.json  # 示例 .claude/settings.json
└── docs/                        # 额外文档
    └── installation.md          # 详细安装指南
```

## 文档

- **[Skill 文档](skill/README.md)** - 完整的 Skill 使用指南
- **[Windows 路径指南](skill/references/windows-paths.md)** - Git Bash 的 Windows 路径转换
- **[环境变量参考](skill/references/environment-variables.md)** - 详细的环境变量配置
- **[安装指南](docs/installation.md)** - 分步安装说明

## 工作原理

### 问题所在

在 Claude Code 的 bash 会话中无法通过标准的 `conda activate` 激活 conda 环境，因为每个命令都在新的非交互式 shell 中运行。

### 解决方案

配置工作区的 `.claude/settings.json`，在 `PATH` 环境变量中优先设置 conda 环境的路径。这样做之所以有效，是因为：

1. Shell 命令使用 PATH 查找可执行文件
2. PATH 中的第一个匹配项会被使用
3. 不需要 shell 初始化

### 优势

- 无需 shell 初始化
- 跨平台工作
- 在所有命令间持久化
- 无子进程开销
- 兼容所有 Claude Code 功能

## 验证脚本

包含的 `validate_env.py` 脚本会检查：

- 环境变量（CONDA_DEFAULT_ENV、CONDA_PREFIX、PATH）
- Python 解释器位置
- 工作区配置文件
- 整体设置状态

随时运行此脚本来验证您的配置：

```bash
python .claude/skills/conda-env-setup/scripts/validate_env.py
```

## 平台注意事项

### Windows

- 使用 Git Bash 格式：`/c/ProgramData/anaconda3` 而非 `C:\ProgramData\anaconda3`
- 仅使用正斜杠，不要使用反斜杠
- 包含 `/Scripts` 目录以获取 Windows 可执行文件

### Linux/macOS

- 标准 Unix 路径
- 包含 `/bin` 目录以获取可执行文件

## 故障排除

### 找不到环境中的 Python

1. 验证 PATH 条目是否正确
2. 检查路径语法错误
3. 确保 `.claude/settings.json` 是有效的 JSON
4. 重启 Claude Code

### 找不到包

1. 验证 PYTHONPATH 包含环境的 site-packages
2. 检查包是否安装在 conda 环境中
3. 运行验证脚本

### 配置未生效

1. 确认 `.claude/settings.json` 在工作区根目录
2. 验证 JSON 语法
3. 检查是否有冲突的全局设置
4. 重启 Claude Code

## 贡献

欢迎贡献！请随时提交 Pull Request。

## 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。

## 致谢

- 为使用 conda 环境的 Claude Code 用户创建
- 灵感来源于对 AI 辅助开发中可靠 Python 环境配置的需求

## 支持

如有问题、建议或想法，请：
- 在 GitHub 上提 Issue
- 查看[文档](skill/README.md)
- 运行验证脚本进行诊断

## 相关项目

- [Claude Code](https://github.com/anthropics/claude-code) - Claude Code 官方仓库
- [Conda](https://docs.conda.io/) - Conda 官方文档

---

**注意**：此 Skill 专为 Claude Code 设计。使用前请确保已安装 Claude Code。

## 快速链接

- **[GitHub 仓库](https://github.com/fucheng830/claude-code-conda-env-setup)**
- **[Issue 跟踪](https://github.com/fucheng830/claude-code-conda-env-setup/issues)**
- **[v1.0.0 Release](https://github.com/fucheng830/claude-code-conda-env-setup/releases/tag/v1.0.0)**
