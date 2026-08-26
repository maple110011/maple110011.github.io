---
permalink: /notes/
title: "笔记"
excerpt: "学习笔记与思考"
author_profile: true
---

<span class='anchor' id='notes'></span>

## 笔记

这里收录我的学习笔记，涵盖数学、概率论、统计学与机器学习等领域。

### 按标签筛选

<div class="tag-filter" id="tag-filter">
  <span class="tag active" data-tag="all">全部</span>
  <span class="tag" data-tag="数学">数学</span>
  <span class="tag" data-tag="概率论">概率论</span>
  <span class="tag" data-tag="测度论">测度论</span>
  <span class="tag" data-tag="最优传输">最优传输</span>
  <span class="tag" data-tag="Wasserstein距离">Wasserstein距离</span>
  <span class="tag" data-tag="抽象代数">抽象代数</span>
  <span class="tag" data-tag="等价关系">等价关系</span>
  <span class="tag" data-tag="证明技巧">证明技巧</span>
</div>

### 笔记列表

<ul class="note-list" id="note-list">
{%- assign items = site.notes | sort: 'date' | reverse -%}
{%- for p in items %}
  <li class="note-list-item" data-tags="{{ p.tags | join: ',' }}">
    <div class="note-title"><a href="{{ p.url }}">{{ p.title }}</a></div>
    {% if p.excerpt %}<div class="note-excerpt">{{ p.excerpt }}</div>{% endif %}
    <div class="note-meta">
      <span class="tag">{{ p.date | date: '%Y-%m-%d' }}</span>
      {%- for t in p.tags %} <span class="tag">{{ t }}</span>{% endfor %}
    </div>
  </li>
{% endfor -%}
</ul>

<script>
(function() {
  var filter = document.getElementById('tag-filter');
  var items = document.querySelectorAll('#note-list .note-list-item');
  if (!filter || !items.length) return;

  filter.addEventListener('click', function(e) {
    var tag = e.target.getAttribute('data-tag');
    if (!tag) return;

    // Update active state
    filter.querySelectorAll('.tag').forEach(function(t) {
      t.classList.remove('active');
    });
    e.target.classList.add('active');

    // Filter items
    items.forEach(function(item) {
      if (tag === 'all') {
        item.classList.remove('filtered-out');
      } else {
        var itemTags = item.getAttribute('data-tags') || '';
        if (itemTags.indexOf(tag) !== -1) {
          item.classList.remove('filtered-out');
        } else {
          item.classList.add('filtered-out');
        }
      }
    });
  });
})();
</script>
