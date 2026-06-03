# GitHub Pages Blog

这是一个可以直接部署到 GitHub Pages 的 Jekyll 博客模板。

## 使用步骤

1. 在 GitHub 新建一个公开仓库，仓库名建议使用：

   ```text
   qianbei333.github.io
   ```

2. 在本地进入这个目录：

   ```bash
   cd /Users/liuzhi/Documents/github-blo
   ```

3. 设置远程仓库地址：

   ```bash
   git remote add origin https://github.com/qianbei333/qianbei333.github.io.git
   ```

4. 推送：

   ```bash
   git push -u origin main
   ```

5. 打开 GitHub 仓库的 `Settings -> Pages`，选择从 `main` 分支部署。

部署完成后，访问：

```text
https://qianbei333.github.io
```

## 写新文章

在 `_posts` 目录中新建 Markdown 文件，文件名格式：

```text
YYYY-MM-DD-title.md
```

文章头部格式：

```markdown
---
layout: post
title: "文章标题"
date: 2026-06-03 10:00:00 +0800
categories: blog
---
```
