# Pica Skills

Gemini CLI 自动化工作流技能库。

### 🚀 现有技能

#### 1. [xhs-browser-poster](./xhs-browser-poster/)
自动化小红书发帖（含 AI 配图）。
- **特性**: Gemini AI 绘图, 自动上传发布, 发布状态校验, 笔记管理页数据抓取。
- **用法**:
  - **取数据**: `python xhs-browser-poster/scripts/get_note_manager_data.py --format json`
  - **生图**: `python xhs-browser-poster/scripts/generate_gemini_img.py "提示词"`
  - **发帖**: `python xhs-browser-poster/scripts/post_to_xhs.py "图片路径" "标题" "正文"`

### 🛠️ 环境要求
- Python 3.8+, 需开启 Chrome/Edge 远程调试端口 (`--remote-debugging-port=9222`)。
- `pip install playwright beautifulsoup4`

---

## 🔧 AI Agent 安装指南

使用以下命令将技能直接安装到您的 Gemini CLI。

```bash
# 示例：安装 xhs-browser-poster 技能
mkdir -p ~/.gemini/skills/xhs-browser-poster/scripts
curl -L https://raw.githubusercontent.com/picasso250/pica-skills/main/xhs-browser-poster/SKILL.md -o ~/.gemini/skills/xhs-browser-poster/SKILL.md
curl -L https://raw.githubusercontent.com/picasso250/pica-skills/main/xhs-browser-poster/scripts/get_note_manager_data.py -o ~/.gemini/skills/xhs-browser-poster/scripts/get_note_manager_data.py
curl -L https://raw.githubusercontent.com/picasso250/pica-skills/main/xhs-browser-poster/scripts/post_to_xhs.py -o ~/.gemini/skills/xhs-browser-poster/scripts/post_to_xhs.py
curl -L https://raw.githubusercontent.com/picasso250/pica-skills/main/xhs-browser-poster/scripts/generate_gemini_img.py -o ~/.gemini/skills/xhs-browser-poster/scripts/generate_gemini_img.py
```

## 📜 许可证
MIT
