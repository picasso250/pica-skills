---
name: xhs-browser-poster
description: Automates Xiaohongshu (XHS) posting via browser. Includes two robust scripts: one for generating high-res images in Gemini (including Tool selection) and one for publishing to XHS and verifying via the Note Manager.
---

# XHS Browser Poster

Automate Xiaohongshu publishing with AI-generated images.

## Prerequisite
- User already logged into Xiaohongshu and Gemini.

## Core Scripts

### 1. Gemini Image Generation
Use `scripts/generate_gemini_img.py` to generate and download an image.
- **Input**: Prompt string.
- **Workflow**: Navigates to Gemini, clicks "Tools" -> "Create Image", waits 60s for generation, and downloads the high-res file.
- **Output**: Prints `RESULT_IMAGE_PATH:<path>`.

```bash
python scripts/generate_gemini_img.py "A cozy afternoon tea at a street cafe, natural lighting, shot on phone."
```

### 2. XHS Posting & Verification
Use `scripts/post_to_xhs.py` to publish and verify.
- **Input**: Image path, Title, and Content.
- **Workflow**: Navigates to the publish page, uploads image, fills title/content, clicks Publish, and then reloads the Note Manager to confirm the post's presence.
- **Output**: Prints `VERIFICATION_SUCCESS` and a JSON string `RESULT_NOTES_DATA` containing titles in the manager.

```bash
python scripts/post_to_xhs.py "image.jpg" "Title" "Content"
```

## Best Practices
- **Hashtags**: Always ensure a space after each hashtag in the content string.
- 你应当先使用 skills\xhs-browser-poster\scripts\get_note_manager_data.py 获取管理数据，找到最高浏览量的那条，然后在发布时使用相似的标题和内容，以提高曝光率。