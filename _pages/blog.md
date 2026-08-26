---
permalink: /blog/
title: "日志"
excerpt: "随笔与实验记录"
author_profile: true
---

<span class='anchor' id='blog'></span>

## 日志

比笔记更松散的记录：实验复盘、学习片段、一时一地的想法。未必严谨，但求真实。

<ul class="note-list">
{%- assign items = site.logs | sort: 'date' | reverse -%}
{%- for p in items %}
  <li class="note-list-item">
    <div class="note-title"><a href="{{ p.url }}">{{ p.title }}</a></div>
    {% if p.excerpt %}<div class="note-excerpt">{{ p.excerpt }}</div>{% endif %}
    <div class="note-meta">
      <span class="tag">{{ p.date | date: '%Y-%m-%d' }}</span>
      {%- for t in p.tags %} <span class="tag">{{ t }}</span>{% endfor %}
    </div>
  </li>
{% endfor -%}
</ul>

{% if site.logs.size == 0 %}
> 暂无日志。
{% endif %}
