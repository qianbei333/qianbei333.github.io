---
layout: default
title: Home
---

<section class="hero">
  <p class="eyebrow">Personal Blog</p>
  <h1>Research notes, technical writing, and personal reflections.</h1>
  <p class="lead">A place for paper notes, project records, coding experience, and essays.</p>
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
