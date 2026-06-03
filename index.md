---
layout: default
title: Home
---

<section class="hero">
  <p class="eyebrow">Personal Blog</p>
  <h1>记录研究、技术和日常思考。</h1>
  <p class="lead">这里可以放论文笔记、项目记录、代码经验和个人文章。</p>
</section>

<section class="post-list">
  <h2>Latest Posts</h2>
  {% for post in site.posts %}
    <article class="post-card">
      <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%Y-%m-%d" }}</time>
      <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
      {% if post.excerpt %}
        <p>{{ post.excerpt | strip_html | truncate: 120 }}</p>
      {% endif %}
    </article>
  {% endfor %}
</section>
