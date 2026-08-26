---
permalink: /translations/
title: "译介"
excerpt: "学术文献翻译"
author_profile: true
---

<span class='anchor' id='translations'></span>

## 译介

这里收录我对英文学术文献的翻译与解读，涵盖贝叶斯统计、深度学习、机器学习等领域的前沿论文。

### 译作列表

<ul class="note-list">
{%- assign items = site.translations | sort: 'date' | reverse -%}
{%- for p in items %}
  <li class="note-list-item">
    <div class="note-title"><a href="{{ p.url }}">{{ p.title }}</a></div>
    {% if p.excerpt %}<div class="note-excerpt">{{ p.excerpt }}</div>{% endif %}
    <div class="note-meta">
      <span class="tag">{{ p.date | date: '%Y-%m-%d' }}</span>
      {%- for t in p.tags %} <span class="tag">{{ t }}</span>{% endfor %}
      {%- if p.original %} <span class="note-meta-src">原文：{{ p.original }}</span>{% endif %}
    </div>
  </li>
{% endfor -%}
</ul>
