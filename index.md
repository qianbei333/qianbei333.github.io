---
layout: default
title: Home
---

<section class="hero">
  <p class="eyebrow">Personal Blog</p>
  <h1>Hello, I am Liu Zhi.</h1>
  <p class="lead">I am a PhD student at Xiangya Hospital, Central South University, focusing on single-cell omics, GWAS, and integrative computational approaches to biomedical research.</p>
  <p class="lead">Email: <a href="mailto:liuzhi@csu.edu.cn">liuzhi@csu.edu.cn</a></p>
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
