---
name: screenshot
description: 使用 Playwright 截取网页屏幕截图的技能。
---

这个技能使用 Playwright 来截取网页（远程或本地）的屏幕截图。

```bash
python3 /root/.gemini/skills/screenshot/screenshot.py <output_file> <url_or_path> [--dir <server_directory>] [--timeout <seconds>]
```

例如：

**截取本地文件：**
```bash
python3 /root/.gemini/skills/screenshot/screenshot.py result.png /index.html --dir ./dist
```

**截取远程 URL：**
```bash
python3 /root/.gemini/skills/screenshot/screenshot.py result.png https://www.google.com
```

**等待几秒后再截图：**
```bash
python3 /root/.gemini/skills/screenshot/screenshot.py result.png /index.html --dir ./dist --timeout 5
```
