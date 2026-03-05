---
name: screenshot
description: 使用 Playwright 截取网页屏幕截图的技能。
---

这个技能使用 Playwright 来截取网页（远程或本地）的屏幕截图。

```bash
python3 /root/.gemini/skills/screenshot/screenshot.py <output_file> <url_or_path> [--dir <server_directory>] [--timeout <seconds>] [--mobile]
```

例：
```bash
python3 /root/.gemini/skills/screenshot/screenshot.py screenshot.png / --dir ./dist --timeout 5
```

更详细的使用说明请参阅 [screenshot.py](screenshot.py) 的源码。