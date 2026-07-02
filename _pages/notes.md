---
permalink: /notes
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
  <span class="tag" data-tag="抽象代数">抽象代数</span>
  <span class="tag" data-tag="测度论">测度论</span>
  <span class="tag" data-tag="概率论">概率论</span>
  <span class="tag" data-tag="最优传输">最优传输</span>
  <span class="tag" data-tag="Wasserstein距离">Wasserstein距离</span>
  <span class="tag" data-tag="贝叶斯深度学习">贝叶斯深度学习</span>
  <span class="tag" data-tag="统计计算">统计计算</span>
</div>

### 笔记列表

<ul class="note-list" id="note-list">
  <li class="note-list-item" data-tags="数学,最优传输,测度论">
    <div class="note-title"><a href="/notes/optimal-transport-1">最优传输笔记（一）：Monge问题、Kantorovich松弛与Wasserstein距离</a></div>
    <div class="note-excerpt">从Monge问题出发，引入Kantorovich松弛与coupling概念，证明KOT的紧性与存在性，定义Wasserstein距离并证明其度量性质与上界估计。</div>
    <div class="note-meta">
      <span class="tag" style="font-size:0.8em;">数学</span>
      <span class="tag" style="font-size:0.8em;">最优传输</span>
      <span class="tag" style="font-size:0.8em;">测度论</span>
    </div>
  </li>
  <li class="note-list-item" data-tags="数学,最优传输,Wasserstein距离">
    <div class="note-title"><a href="/notes/optimal-transport-2">最优传输笔记（二）：KOT解的存在性、Wasserstein距离的性质与上界估计</a></div>
    <div class="note-excerpt">深入研究KOT解的存在性条件，证明Wasserstein距离的度量公理（非负性、对称性、正定性、三角不等式），并建立Wasserstein距离与全变差距离之间的控制不等式。</div>
    <div class="note-meta">
      <span class="tag" style="font-size:0.8em;">数学</span>
      <span class="tag" style="font-size:0.8em;">最优传输</span>
      <span class="tag" style="font-size:0.8em;">Wasserstein距离</span>
    </div>
  </li>
  <li class="note-list-item" data-tags="数学,抽象代数">
    <div class="note-title"><a href="/notes/equivalence-relation">等价关系与商集</a></div>
    <div class="note-excerpt">从分类的思想出发，探讨等价关系与商集的基本概念，以及第一同构定理的普遍形式。</div>
    <div class="note-meta">
      <span class="tag" style="font-size:0.8em;">数学</span>
      <span class="tag" style="font-size:0.8em;">抽象代数</span>
    </div>
  </li>
  <li class="note-list-item" data-tags="数学,测度论,概率论">
    <div class="note-title"><a href="/notes/good-set-principle">好集原理</a></div>
    <div class="note-excerpt">测度论与概率论中一种重要的证明技巧——好集原理的形式化描述与典型应用，以及 $\pi-\lambda$ 定理的证明。</div>
    <div class="note-meta">
      <span class="tag" style="font-size:0.8em;">数学</span>
      <span class="tag" style="font-size:0.8em;">测度论</span>
      <span class="tag" style="font-size:0.8em;">概率论</span>
    </div>
  </li>
  <li class="note-list-item" data-tags="数学,概率论,测度论">
    <div class="note-title"><a href="/notes/random-variable">为什么随机变量是定义在样本空间上的实值可测函数</a></div>
    <div class="note-excerpt">深入解读随机变量的严格定义，阐述如何通过可测映射将抽象概率空间的分析转移到熟悉的实数空间上。</div>
    <div class="note-meta">
      <span class="tag" style="font-size:0.8em;">数学</span>
      <span class="tag" style="font-size:0.8em;">概率论</span>
      <span class="tag" style="font-size:0.8em;">测度论</span>
    </div>
  </li>
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
