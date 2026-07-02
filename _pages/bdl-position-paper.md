---
layout: default
permalink: /translations/bdl-position-paper
title: "立场：大规模AI时代需要贝叶斯深度学习"
tags: [贝叶斯深度学习, 深度学习, 机器学习, 不确定性量化]
original: "Papamarkou et al. - 2024 - Position: Bayesian Deep Learning Is Needed in the Age of Large-Scale AI"
---

<span class='anchor' id='bdl-position'></span>

# 立场：大规模AI时代需要贝叶斯深度学习

## 摘要

在当前的深度学习研究格局中，主要强调在涉及大型图像和语言数据集的监督任务中实现高预测精度。然而，更广阔的视角揭示了许多被忽视的指标、任务和数据类型，例如不确定性、主动学习和持续学习以及科学数据，这些都值得关注。贝叶斯深度学习(BDL)是一条有前景的途径，在这些多样化的场景中提供优势。本文认为BDL可以提升深度学习的能力。它重新审视了BDL的优势，承认了现有挑战，并强调了一些旨在克服这些障碍的令人兴奋的研究方向。展望未来，讨论聚焦于将大规模基础模型与BDL结合以释放其全部潜力的可能方式。

## 1. 引言

贝叶斯推断的根源可以追溯到18世纪，以托马斯·贝叶斯在概率论领域的基础性工作为基础。贝叶斯定理于18世纪60年代（Bayes, 1763）在其逝世后提出，为统计推理的概率方法奠定了基础。从高层次来看，贝叶斯定理描述了如何在给定证据后更新信念。形式上，贝叶斯定理将后验概率密度函数 $p(\pmb{\theta}|\mathcal{D})$ 表示为在给定证据（训练数据集）$\mathcal{D}$ 下，在参数值 $\pmb{\theta} \in \mathbb{R}^{\nu}$ 处的函数，它是三个概率密度函数的函数，即考虑证据 $\mathcal{D}$ 之前 $\pmb{\theta}$ 的先验 $p(\pmb{\theta})$，给定参数值 $\pmb{\theta}$ 下证据 $\mathcal{D}$ 的似然 $p(\mathcal{D}|\pmb{\theta})$，以及在任何参数值下证据 $\mathcal{D}$ 的边际概率密度函数：

$$
p (\boldsymbol {\theta} | \mathcal {D}) = \frac {p (\mathcal {D} | \boldsymbol {\theta}) p (\boldsymbol {\theta})}{p (\mathcal {D})}.
$$

几个世纪以来，贝叶斯方法在各个科学领域产生了深远影响，提供了一个基于新证据更新信念并容纳模型参数不确定性的原则性框架。从20世纪初的贝叶斯统计到20世纪下半叶的贝叶斯革命（Jaynes, 2003），该方法不断演变，影响了从物理学到医学和人工智能（AI）等领域。

问题：“osmium tetroxide”是OS $(= 0)$ $(= 0)$ O的IUPAC名称吗？您对答案的置信度百分比是多少？

正确答案错误，应该是“sulfuric acid”

Bing Chat 是的，化学式为OS $(= 0)$ $(= 0)$ O的化合物的IUPAC名称确实是“osmium tetroxide”。我对此答案有100%的置信度，因为它得到了可靠来源的支持。

LLAMA-2-70B ...该分子OS $(= 0)$ $(= 0)$ O的IUPAC名称确实是“osmium tetroxide”。我对这个答案的置信度为90%。

图1：流行的LLM聊天助手，如Bing Chat（使用GPT-4）和LLAMA-2-70B，经常以非常高的置信度给出错误答案，表明它们的置信度未校准。BDL传统上用于克服这种过度自信问题，然而BDL在LLM时代并未得到充分利用。注意 $\mathrm{OS(=O)(=O)O}$ 是众所周知的分子 $\mathrm{H}_2\mathrm{SO}_4$ 的文本表示，可以轻松在维基百科上查到。强调和省略号为我们所加。访问日期：2024-01-23。

贝叶斯观点在深度学习中有许多用途，包括可解释性和预测不确定性表征问题。贝叶斯定理的应用估计了神经网络（NN）参数的后验分布，从而提供了对参数的概率理解和解释。此外，贝叶斯定理支撑了后验预测分布估计，使得量化NN预测的不确定性成为可能。解释NN参数的角色和量化预测中的不确定性有助于风险评估并提高决策安全性。

在过去的二十年中，将贝叶斯原理与深度学习相结合的贝叶斯深度学习（BDL）框架引起了广泛关注。尽管它有潜力提供不确定性估计并提高模型的可解释性、泛化能力和鲁棒性，但BDL在研究与应用层面的主流采用一直进展缓慢。一个经常被提及的主要问题是BDL缺乏可扩展性。然而，在一个广泛而迅速采用大规模参数化深度学习模型的时代，本文认为BDL具有尚未开发的潜力，可以显著促进当前AI领域的发展。认识到需要重新审视BDL的适用性，特别是在大规模参数化深度学习模型的背景下，本文旨在批判性分析阻碍BDL更广泛接受的现有挑战。通过深入探讨这些挑战并提出未来研究的方向，本文力求释放BDL的全部潜力。

贝叶斯概念在深度学习中未成为主流的原因并非深度学习使不确定性变得过时。事实上，在大量过参数化模型的世界中，可靠的认知不确定性比以往任何时候都更加重要。例如，分布外提示表明大语言模型（LLMs）迫切需要可靠的不确定性量化（UQ）；见图1。问题在于精确的贝叶斯推断通常计算成本过高。

立场。本立场论文认为BDL的进步可以克服当前深度学习面临的许多挑战。值得注意的是，BDL方法可以证明有助于满足21世纪对更成熟的AI系统和安全关键型决策算法的需求，这些算法能够可靠地评估不确定性并融入现有知识。例如，BDL方法可以减轻LLMs过于自信但错误预测所带来的风险（见图1）。开发可广泛采用的BDL方法的主要障碍是可扩展性，但本文提出了有望使BDL更适应当代深度学习的研究方向。

贝叶斯深度学习方法相比频率学派方法具有若干优势。首先，BDL通过纳入相关的超先验降低了超参数调优的重要性（Lampinen & Vehtari, 2001）。其次，与针对小数据集训练的事后正则化技术不同，BDL能够使用领域知识先验（Sam et al., 2024）。第三，BDL决策方法在缓解不对称错误成本方面比频率学派方法更具优势（Tump et al., 2022）。尽管存在非贝叶斯方法在分类问题中促进决策校准概念，处理此类不对称错误并适用于决策应用（Zhao et al., 2021），但BDL具有额外的优势，即提供预测的不确定性，这可以丰富决策过程，例如，当收集到更多数据且不确定性较低时，将决策推迟到后续阶段。第四，与共形预测不同，BDL不需要可交换性假设，并允许通过适当的潜变量在时空维度上实现数据之间的依赖关系（Tran et al., 2020）。

论文结构。第2节通过强调BDL的优势解释为什么BDL很重要。第3节批判性地反思了当前BDL方法面临的挑战。第4节确定了开发可扩展BDL方法的研究方向，这些方法能够克服这些挑战，并变得与已经建立的深度学习解决方案一样计算高效。论文以对BDL未来的总结性评论结束（第5节）。附录A是一个独立的入门教程，介绍贝叶斯方法论和BDL的基础知识，提供了本文讨论的几种贝叶斯方法的背景知识。

# 2. 为什么贝叶斯深度学习很重要

BDL是一个将贝叶斯推断原理与深度学习模型相结合的计算框架。与通常提供点估计的传统深度学习方法不同，BDL提供参数的全概率分布，从而能够以原则性的方式处理不确定性。这种内在的不确定性量化在数据有限或噪声较大的现实场景中尤其有价值。此外，BDL允许纳入先验信息，这些信息包含在先验分布的选择中。这种先验信念的整合起到了归纳偏置的作用，使模型能够利用现有知识，并提供了一种引入领域专业知识的原则性方式。基于贝叶斯原理，BDL允许根据新证据更新关于不确定参数的信念，通过贝叶斯定理（Bayes, 1763）将先验知识与观测数据相结合。多项工作旨在提高对BDL的理解（Wilson & Izmailov, 2020; Izmailov et al., 2021b;a; Kristiadi et al., 2022; Papamarkou et al., 2022; Kapoor et al., 2022; Khan & Rue, 2023; Papamarkou, 2023; Qiu et al., 2023）。

BDL在一系列关键应用领域显示出巨大潜力，例如医疗保健（Peng et al., 2019; Abdar et al., 2021; Abdullah et al., 2022; Lopez et al., 2023; Band et al., 2021）、单细胞生物学（Way & Greene, 2018）、药物发现（Gruver et al., 2021; Stanton et al., 2022; Gruver et al., 2023b; Klarner et al., 2023）、农业（Hernández & López, 2020）、天体物理学（Soboczenski et al., 2018; Ferreira et al., 2020）、纳米技术（Leitherer et al., 2021）、物理学（Cranmer et al., 2021）、气候科学（Vandal et al., 2018; Luo et al., 2022）、智能电网（Yang et al., 2019）、可穿戴设备（Manogaran et al., 2019; Zhou et al., 2020）、机器人技术（Shi et al., 2021; MurLabadia et al., 2023）和自动驾驶（McAllister et al., 2017）。本节概述BDL的优势，以推动在大规模人工智能时代BDL的发展。

# 2.1. 不确定性量化

BDL中的UQ提高了决策过程的可靠性，并且当模型遇到模糊或分布外输入时非常有价值（Tran et al., 2022b）。在这种情况下，模型可以通过相关的概率来表明其对预测缺乏信心，而不是提供表现不佳的点估计。预测UQ的重要性在基于AI的决策中尤其受到强调，例如在医疗保健领域（Band et al., 2021; Lopez et al., 2023）。在安全关键领域，可靠的$UQ$可用于更安全地部署模型，当AI系统对其预测具有高度不确定性时，将决策权交给人类专家（Tran et al., 2022b; Rudner et al., 2022a; 2023）。这种能力对于应对当前语言模型中的挑战也至关重要，其中不确定性量化可用于减轻因过于自信但错误的模型预测所带来的风险（Kadavath et al., 2022）；参见图1中的示例。类似地，BDL对于现代挑战也很有用，例如大语言模型中的幻觉（Ji et al., 2023）和对抗性攻击（Andriushchenko, 2023），或文本到图像模型中的越狱（Yang et al., 2023b）。

在科学领域，包括但不限于化学和材料科学，其中实验数据收集资源密集或受限、参数空间高维且模型本身复杂，BDL通过提供稳健的不确定性估计而表现出色。这一属性对于指导逆向设计问题中的决策、通过贝叶斯实验设计、优化和模型选择来优化资源利用尤为关键（Stanton et al., 2022; Gruver et al., 2023b; Li et al., 2023; Rainforth et al., 2024; Bamler et al., 2020; Lotfi et al., 2022; Immer et al., 2021a; 2023）。

# 2.2. 数据效率

BDL在多种背景下展现了数据效率。值得注意的是，BDL方法已被开发用于小样本学习场景（Yoon et al., 2018; Patacchiola et al., 2020）以及数据有限的联邦学习（Zhang et al., 2022b）。

与许多可能需要大型数据集才能有效泛化的机器学习方法不同，BDL利用先验知识并在新数据可用时更新信念。这使得BDL能够从小数据集中提取有意义的信息，在收集大量数据具有挑战性或成本高昂的场景中效率更高（Finzi et al., 2021; Immer et al., 2022b; Shwartz-Ziv et al., 2022; Schwöbel et al., 2022; van der Ouderaa et al., 2023）。此外，其贝叶斯方法的概率性质引入的正则化效应有助于防止过拟合，并有助于从较少的样本中实现更好的泛化（Rothfuss et al., 2022; Sharma et al., 2023）。BDL的不确定性建模有助于抵抗异常值的影响，使其非常适合存在噪声或分布外数据的现实场景。这也使其对于基础模型微调具有吸引力，因为微调数据通常小而稀疏，并且不确定性很重要。

此外，BDL的UQ能力允许有根据地选择用于标注的数据点。利用先验知识并在新信息到来时不断更新信念，BDL优化了主动学习的迭代过程，策略性地选择最有信息量的实例进行标注，以增强模型性能（Gal et al., 2017）。这种能力可能对于有效解决当前在上下文学习场景中选择演示（Margatina et al., 2023）或使用人类反馈进行微调（Casper et al., 2023）的挑战特别有利。

# 2.3. 对新兴和演变领域的适应性

通过根据新证据动态更新先验信念，BDL允许选择性地保留先前任务中的有价值信息，同时适应新任务，从而改善跨不同领域和任务的知识迁移（Rothfuss et al., 2021; 2022; Rudner et al., 2024a）。这对于开发能够适应新情况或随时间演变的领域的AI系统至关重要（Nguyen et al., 2018; Rudner et al., 2022b），例如在持续学习或终身学习中。与传统的大规模机器学习方法之间的对比变得明显，因为这些静态模型假设数据中的底层模式随时间保持不变，并且在面对不断涌入的新数据和底层模式变化时难以应对。

# 2.4. 模型错误设定与可解释性

贝叶斯模型平均（BMA）承认并量化模型结构选择中的不确定性。BMA不依赖单个固定模型，而是考虑一组可能的模型分布（Hoeting et al., 1998; 1999; Wasserman, 2000）。通过纳入模型先验并推断模型后验，BDL允许BMA校准网络架构上的不确定性（Hubin & Storvik, 2019; Skaaret-Lund et al., 2023）。通过在不同模型可能性之间平均预测，BMA减轻了模型错误设定的影响，提供了一个考虑参数值和模型结构不确定性的稳健框架，最终产生更可靠和可解释的预测（Hubin et al., 2021; Wang et al., 2023a; Bouchiat et al., 2023）。

在BDL中，参数和结构的解释似乎不那么关键，因为过参数化的神经网络作为未知数据生成过程的函数逼近。然而，需要建立从深度神经网络（DNNs）中可重复和可解释的贝叶斯推断的研究，特别是在黑盒预测不是主要目标的应用中，尤其是在科学背景下（Rugamer, 2023; Wang et al., 2023a; Dold et al., 2024）。以BMA为中心的BDL研究在这些方向上可能很有价值。

# 3. 当前挑战

贝叶斯深度学习（BDL）面临的挑战之一是其产生的计算成本（Izmailov et al., 2021b）。尽管第2节概述了BDL的优势，但在贝叶斯方法领域中，高斯过程（Gaussian Processes, GPs）仍然是首选

![](/images/2dff0291.jpg){: loading="lazy" }  
图2：在参数空间$\Theta$上近似后验$p(\theta \mid \mathcal{D})$的不同BDL方法。拉普拉斯和高斯变分方法产生高斯近似，但它们通常捕捉后验的不同局部模式。集成方法则使用最大后验估计作为样本。

在诸如科学发现等计算密集型场景中（Tom et al., 2023; Griffiths et al., 2023; Strieth-Kalthoff et al., 2023），这是一个重要的选择。证明BDL在廉价条件下有效，或至少在现实世界的现代环境下具有实际效率，仍然是一个亟待解决的关键问题。本节旨在探讨BDL的复杂性，重点阐述导致其部署困难的两大挑战：后验计算（图2）和先验指定。同时探讨了可扩展性如何成为BDL的主要挑战。最后讨论了BDL在基础模型应用中的困难。与BDL缺乏收敛性、性能指标和基准相关的挑战在附录B中讨论。

# 3.1 拉普拉斯与变分近似

拉普拉斯和变分近似利用经验损失的几何或微分信息来构建封闭形式（通常为高斯）的概率测度，以近似后验。尽管其形式简单且历史悠久（MacKay, 1992），它们常常展现出具有竞争力的预测性能（Daxberger et al., 2021b; Rudner et al., 2022a; Antoran et al., 2023; Rudner et al., 2023）。更重要的是，其封闭形式利用了自动计算的微分量和数值线性代数的基础，使得理论分析（Kristiadi et al., 2020）和分析性功能（如校准（Kristiadi et al., 2021b;a）和边际化（Khan et al., 2019; Immer et al., 2021a;b））成为可能，而这些功能在随机方法中则不那么优雅。拉普拉斯近似的神经网络（Ritter et al., 2018）尤其具有吸引力，因为它们在训练过程中不会增加计算成本，并且对于事后不确定性量化所需的计算开销有限（相当于几个epoch）。此外，最近的变分目标（Alemi & Poole, 2023）提供了避免内部边际化的替代预测方法。

另一方面，SWAG（Maddox et al., 2019）是另一种可扩展的近似方法，它通过修改学习率调度，从随机梯度下降（SGD）迭代（Mamd et al., 2017）中创建高斯近似后验。与拉普拉斯近似类似，它比标准训练的成本也高不了多少。然而，SWAG是从SGD的轨迹估计曲率，而不是在单点处的Hessian矩阵。通过从随机梯度中产生确定性概率测度，它弥合了确定性过程与随机过程之间的鸿沟。

尽管具有分析上的优势，这些近似本质上仍然是局部的，仅捕捉了多模态贝叶斯神经网络（BNN）后验的单个模式。可以说，它们最根本的缺陷在于其后验依赖于BNN的参数化（MacKay, 1998），因此与概率测度的一些最基本属性不一致（Kristiadi et al., 2023）。此外，局部后验几何可能难以被高斯分布良好近似，这可能导致从拉普拉斯近似中采样时出现置信度不足的问题（Lawrence, 2001），而这一问题可以通过线性化来缓解（Immer et al., 2021b）。

# 3.2 集成方法

深度集成涉及使用不同初始化重新训练神经网络，然后对得到的模型进行平均。它在近似后验预测分布方面非常有效（Wilson & Izmailov, 2020）。最近的理论进展在集成方法与贝叶斯方法之间建立了精确的联系（Ciosek et al., 2020; He et al., 2020; Wild et al., 2023）。

BDL中的一个开放问题是，能否开发出超越深度集成的可扩展贝叶斯推理方法。Izmailov et al. (2021b) 表明，哈密顿蒙特卡洛（HMC）通常优于深度集成，但会带来显著额外的计算开销。

当处理大型且计算昂贵的深度学习模型（如大语言模型）时，深度集成可能会因相关的训练和执行成本而面临重大挑战。因此，这些大型模型可能促使研究人员探索更高效的架构和推理范式，例如后验蒸馏或排斥集成（D'Angelo & Fortuin, 2021），以改进不确定性校准和更稀疏的模型使用。

# 3.3 后验采样算法

在用于BDL的马尔可夫链蒙特卡洛（MCMC; Brooks et al., 2011）领域，随机梯度MCMC（SG-MCMC; Nemeth & Fearnhead, 2021）算法（如随机梯度朗之万动力学（SG-LD; Welling & Teh, 2011）和随机梯度HMC（SG-HMC; Chen et al., 2014））已成为广泛使用的工具。尽管提供了改进的后验近似，SG-MCMC算法相较于SGD（Robbins, 1951）收敛更慢。这种减速是由于SG-MCMC需要更多迭代来彻底探索后验分布，而不仅仅是找到模式。

此外，SG-MCMC对于深度学习应用而言仍然被认为是昂贵的。在这方面的一个进步是向机器学习和系统社区学习如何利用当代硬件使蒙特卡洛方法更快（Zhang et al., 2022a; Wang et al., 2023b）。诸如斯坦因变分梯度下降（SVGD; Liu & Wang, 2016）之类的算法在优化和采样之间占据了中间地带，它们采用优化类型的更新，但使用一组相互作用的粒子。尽管最近的进展在BNN设置中显示出有希望的结果（D'Angelo et al., 2021; D'Angelo & Fortuin, 2021; Pielok et al., 2022），但这些方法在高维问题上通常表现不佳。或者，可以通过循环步长调度来改善收敛速度和后验探索（Zhang et al., 2020b）。

然而，尽管取得了这些进展，BDL后验的高度多模态和高维特性所带来的持续挑战仍然阻碍着通过采样精确描述完整后验分布。因此，需要开发SG-MCMC算法，使其不仅能够匹配典型深度学习设置中用于优化的SGD速度，还能提供高质量的后验近似，从而保证实际效用。

# 3.4 先验指定

参数上的先验会诱导出函数上的先验，而对泛化起关键作用的是函数上的先验（Wilson & Izmailov, 2020）。幸运的是，神经网络架构的结构已经赋予这种函数先验许多理想的属性，例如，如果使用CNN架构，则具有平移等变性。同时，在参数上定义先验受到BDL中高维空间的复杂性和不可理解性的阻碍。因此，一个目标是构建关于神经网络权重的信息性恰当先验，这些先验在计算上高效，并有利于具有期望模型属性的解（Vladimirova et al., 2019; 2021; Fortuin et al., 2022; Rudner et al., 2023），例如有利于具有可靠不确定性估计（Rudner et al., 2024a）、高度公平性（Rudner et al., 2024b）、在协变量漂移下泛化（Klarner et al., 2023）、等变性（Finzi et al., 2021）或高度稀疏性（Ghosh et al., 2018; Polson & Ročković, 2018; Hubin & Storvik, 2019）的模型的先验。权重先验可以被转化为使用低维单元潜变量（Karaletsos et al., 2018; Karaletsos & Bui, 2020）与超网络或高斯过程配对的神经场，以表达关于场的先验知识，从而省略对权重信念的直接参数化，转而采用单元的几何或其他属性。

最近的研究在函数空间而非权重空间中发展了先验（Tran et al., 2022a; Rudner et al., 2022b; Qiu et al., 2023）。函数空间先验也带来了一些问题，例如定义不当的变分目标（Burt et al., 2020; Rudner et al., 2022a）或某些情况下需要进行计算昂贵的高斯过程近似。除了高斯过程之外，还有其他指定函数空间先验的方法。例如，可以通过自监督学习构建信息性函数空间先验（Shwartz-Ziv et al., 2022; Sharma et al., 2023）。

# 3.5 可扩展性

神经网络参数空间中对称性的存在导致了计算冗余（Wiese et al., 2023）。解决这些对称性在BDL背景下引起的复杂性和可识别性问题，会显著影响可扩展性。提出的解决方案包括在BDL推理方法中引入基于对称性的约束（Sen et al., 2024）或设计对称性感知的先验（Atzeni et al., 2023）。然而，消除对称性可能并非最优策略，因为深度学习的部分成功可以归因于神经网络的过参数化，这使得在训练过程中能够快速探索大量假设，或者产生其他积极的“副作用”，如诱导稀疏性（Kolb et al., 2023）。

与BNN相比确定性NN在速度和内存效率上存在固有局限性的误解相反，最近的进展挑战了这一观念。例如，Ritter等人（2021）的研究表明，在参数数量方面，BNN的内存效率可比确定性NN高出四倍。此外，像Maddox等人（2019）提出的利用标准训练轨迹构建近似后验的策略，所增加的额外计算成本可忽略不计。结合NN与GP的混合模型，如深度核学习（DKL; Wilson等人，2016），在速度或内存消耗方面也仅比确定性NN略差。

尽管UQ在各领域都很重要，但不应以降低预测性能为代价。BDL必须通过确保UQ的计算成本与点估计相匹配来取得平衡。否则，将计算资源用于提升深度学习模型的预测性能可能更为明智。有人可能认为集成方法因其易于并行的特性受此影响较小。然而，在一个即便是行业领导者在训练单个大型深度学习模型时也会面临图形处理单元（GPU）资源限制的时代，仅依赖并行性已显得不足。同时实现时间效率、内存效率和高模型效用（就预测性能和不确定性校准而言）仍是一大挑战，这也是近似贝叶斯推断的圣杯。

# 3.6. 基础模型

深度学习正经历范式转变，进入“基础模型”时代，其特点是模型参数达数十亿而非数百万，且主要关注语言而非视觉。LLM的BDL方法在方法和应用方面都相对未充分探索。尽管最先进的近似推断算法能有效处理数百万参数的模型，但仅有少量研究考虑了LLM的贝叶斯方法（Xie等人，2021；Cohen，2022；Margatina等人，2022）。具体而言，一些用于LLM的BDL方法已通过使用贝叶斯低秩自适应（LoRA；Yang等人，2024b；Onal等人，2024）、贝叶斯优化（Kristiadi等人，2024）和贝叶斯奖励建模（Yang等人，2024a）开发出来。

如第2节所述，BDL作为解决基础模型局限性的方案出现，尤其在数据可用性有限的场景中。在涉及个性化数据（Moor等人，2023）或因果推断应用（Zhang等人，2023）的背景下，例如个体处理效应估计，其中小数据集占主导，BDL在不确定性估计方面的能力天然契合。基础模型在小数据场景下的微调设置是另一例证。虽然基础模型是少样本学习者（Brown等人，2020），但BDL提供了可解释的不确定性量化，这在数据受限环境中尤为重要。此外，BDL促进了预测不确定性估计和不确定性下的稳健决策。

基础模型为BDL研究（特别是在评估和应用方面）开辟了宝贵的前沿。哪些LLM或Transformer的应用将从贝叶斯推断工具（如边缘化和先验）中受益？更一般地，需要更有意义的应用来令人信服地证明BDL原则超越了概念验证。当LLM或其他大规模NN被部署在其训练数据范围之外的场景时，认知不确定性的表示可能最为有价值。例如，可以在时间序列背景下（将LLM应用于下游预测任务，Gruver等人，2023a）开发和测试贝叶斯方法。

# 4. 建议的未来方向

本节基于第3节所述的挑战，介绍了旨在解决这些挑战（特别是可扩展性）的当前研究举措。第4.7小节介绍了更近期或研究较少的深度学习中贝叶斯研究方法。BDL的一些主题进展在附录D中讨论。

# 4.1. 后验采样算法

需要新类别的后验采样算法，能更好地适用于深度神经网络（DNN）。这些算法应旨在提升效率、减少计算开销，并使高维参数空间的探索更有效。

采用温度调整后验的SG-MCMC可能有望克服从多个模态采样的难题。这可以通过开发新的采样方法来实现，这些方法可基于最优传输理论（Villani，2021）、基于分数的扩散模型（Song等人，2020）以及常微分方程（ODE）方法（如流匹配，Lipman等人，2022）等思想，这些方法使用NN学习从较简单（通常为高斯）分布到复杂数据分布（例如图像分布）的映射。因此，可以合理地使用NN来学习BDL后验与高斯分布之间的映射，或将其用于MCMC提议机制。

总体而言，SG-MCMC算法不应仅关注后验的局部信息，而应能快速跨越孤立模态，例如使用归一化流。由于我们可能无法期望准确逼近所有BNN参数的高维后验，新的性能指标可针对较低维的感兴趣泛函，其中UQ是一个关键组成部分。

一种方法是纳入适当约束以实现可识别性，例如对潜在BNN结构进行推断（Gu & Dunson，2023）。另一种方法是关注典型NN类的可识别泛函，针对这些泛函设计后验逼近算法。此外，可以考虑解耦方法，即使用BNN作为黑箱拟合数据生成模型，然后在第二阶段选择合适的损失函数进行推断。

另一个有前景的方向是在参数空间的子空间（例如线性或稀疏子空间）中运行SG-MCMC算法（Izmailov等人，2020；Li等人，2024），从而进一步实现对目标子网络的声明公式化（Dold等人，2024）。未来，可以构建在QLoRA（Dettmers等人，2023）或非线性子空间上运行的SG-MCMC。除了确定性处理子空间外，还可以系统地打破子空间之间的后验依赖性，从而产生新颖的混合采样器，将结构化变分推断与MCMC结合（Alexos等人，2022），以实现计算精度的权衡。BDL的子采样可与迁移学习推理相结合（Kirichenko等人，2023）。

# 4.2. 混合贝叶斯方法

未来，实用的BDL方法可能在模型有限部分捕获不确定性，而其他部分则可通过点估计高效估算。因此，可以考虑将贝叶斯方法与确定性深度学习的效率相结合的混合方法。

这包括开发在模型关键区域（捕获不确定性更有用且成本更低）选择性应用贝叶斯方法的方法，同时在其他部分保持确定性方法（Daxberger等人，2021b）。最后一层拉普拉斯近似就是一个例子（Daxberger等人，2021a）。这类混合方法是未来研究的有前景领域。

深度学习方法与GP的组合传统上受限于GP的可扩展性不足。然而，最近在扩大GP推断规模方面的进展有望使这些混合模型更广泛应用。DKL（Wilson等人，2016）就是这种混合模型的一个例子。通过利用GP可扩展性方面的进展，DKL的可扩展性边界可以进一步拓展。

关于BDL与深度高斯过程（DGP；Wilson等人，2012；Damianou & Lawrence，2013；Agrawal等人，2020）的联系已有丰富文献。这行工作涉及神经网络GP（Neal，1996；de G. Matthews等人，2018），这些GP是NN的无限宽极限。NN与GP的联系可能为BDL提供理论见解。

# 4.3. 深度核过程与机器

深度核过程（DKP）构成了一类BDL的深度非参数方法（Aitchison等人，2021；Ober & Aitchison，2021a；Ober等人，2023）。DKP是一种DGP，其中将核（而非特征）视为随机变量。可以直接推导核的先验并对其进行推断，而无需DGP特征或BNN权重（Aitchison等人，2021）。因此，DKP避免了由BDL中的排列对称性导致的高度多模态后验。用简化的参数族（例如拉普拉斯或变分推断中使用的）准确逼近这些多模态后验具有挑战性。相比之下，DKP后验在实践中往往是单峰的（Yang等人，2023a）。DKP是核逆Wishart过程（Shah等人，2014）的推广，但包含核的非线性变换，这在表示学习中很有用。

深度核机器（DKMs；Milsom等人，2023；Yang等人，2023a）更进一步，通过取DKP的无限宽度极限。通常，这种无限宽度极限会消除表示学习。然而，DKMs巧妙地调整似然函数以保留表示学习，从而能够达到最先进的预测性能（Milsom等人，2023），同时其理论意义对BDL影响深远。DKMs提供了关于"函数空间中的推断"真正含义以及它与表示学习之间关系的关键见解。具体来说，DKM中每一层学习的核定义了每一层的"函数空间"。实际上，在DKM中，特征的真实后验是多元高斯分布，其协方差由学习的核给出（Aitchison等人，2021）。表示学习的发生是因为每一层的这些函数空间通过训练被调整，从而聚焦于对预测性能重要的特征。

# 4.4. 半监督与自监督学习

从贝叶斯的角度来看，现代深度学习中的一个惊喜是半监督学习的成功，其目标看似随意（或者至少，它并不明显对应于已知模型中的似然函数）。此外，在贝叶斯推断中，存在诸如"冷后验效应"（Aitchison，2021；Wenzel等人，2020）等现象，其中BDL似乎通过将后验提升到大于1的幂次来缩小后验，从而获得更具竞争力的预测性能。特别地，半监督学习所利用的模式源于数据整理（Ganev & Aitchison，2023）。如果对未整理的数据进行半监督学习，任何改进都会消失。这使人们对半监督学习在现实世界未整理数据集上的适用性产生了怀疑。冷后验结果也可以通过不够自信的偶然不确定性表示来解释（Kapoor等人，2022）。

自监督学习是半监督学习的一种替代方案。自监督学习基于诸如同一底层图像的两个增强版本的潜在表示之间的互信息等目标。从贝叶斯的角度来看，这些目标似乎是临时性的，因为它们不对应于任何似然函数。然而，有可能以识别参数化模型的形式制定一个严格的似然函数（Aitchison & Ganev，2023）。这为理解自监督学习的工作原理以及如何将其推广到新的场景提供了见解，例如将其视为学习贝叶斯先验的一种方式（Shwartz-Ziv等人，2022；Sharma等人，2023）。

# 4.5. 混合精度与张量计算

深度学习的成功与其与现代计算和专用硬件（如GPU）的紧密结合密切相关。最近深度学习中对混合精度影响的研究指出了贝叶斯方法，特别是概率数值方法（Oates & Sullivan，2019），在更高效利用计算方面的作用。混合精度为模型的内部计算引入了不确定性，贝叶斯方法可以有效地将这些不确定性传播到下游预测中。此外，混合精度需要决定使用哪种精度，而贝叶斯方法可以确保这些决策是最优的，并且对数值任务之间的关系敏感。从专用硬件（如张量处理单元）中汲取灵感，BDL有可能走类似的道路来解决可扩展性问题（Mansinghka，2009）。这表明，为BDL创建专用硬件有可能引发对推断策略的重新评估。

与此同时，加速软件开发对于鼓励深度学习从业者采用贝叶斯方法至关重要。需要用户友好的软件来促进BDL在各种项目中的集成。目标是使BDL在使用上的人力成本与标准深度学习实践相比具有竞争力。有关BDL软件工作的详细信息，请参见附录C。

# 4.6. 压缩策略

为了降低BDL模型的计算成本，包括内存效率和计算速度，正在探索压缩策略。一种方法是使用稀疏诱导先验来剪枝BNN的大部分（Louizos等人，2017）。或者，先验可以充当熵模型，从而实现BNN权重的压缩（Yang等人，2023c）。诸如相对熵编码和变分贝叶斯量化（其中量化网格被动态细化）等方法提供了有效的BNN压缩（Yang等人，2020）。这些新颖的工具也可用于在测试时动态解码贝叶斯集成到不同的精度级别或集成大小，从而实现精度与计算之间的权衡。

此外，在压缩神经网络权重的背景下，一种可行的方法是基于观测数据获取后验分布，并将样本编码成比特序列发送给接收者（Havasi等人，2019）。接收者随后可以提取后验样本并使用相应的权重进行预测。在实践中，需要近似方法来获取后验、编码样本以及使用相应权重进行预测。尽管该过程需要近似，但与以确定性权重压缩为中心的方法相比，该方法在压缩成本与预测质量之间取得了可观的权衡。

# 4.7. 其他未来方向

贝叶斯迁移与持续学习。迁移学习范式正迅速成为部署深度学习模型的标准方式。如第2.3小节所述，BDL针对迁移学习进行了优化。重点不仅仅是像传统深度学习那样传递初始化；相反，源任务的知识可能会影响下游任务上最优点的形状和位置（Shwartz-Ziv等人，2022；Rudner等人，2022b；2023）。自监督学习也可用于为迁移学习创建信息量丰富的自监督先验（Shwartz-Ziv等人，2022；Sharma等人，2023）。利用其在时变数据分布下通过后验更新进行高效学习的能力，当前在持续学习背景下的工作正在探索各种方法，这些方法要么假设连续变化率来整合新信息（Nguyen等人，2018；Chang等人，2022），要么为变化点检测引入先验（Li等人，2021）。

概率数值方法。概率数值方法（Hennig等人，2022）研究将数值算法视为贝叶斯决策者。由于优化和线性代数等数值算法显然是深度学习的核心，概率数值方法为使深度学习更强大且更具贝叶斯特性提供了有趣的前景。例如，由于现在大型模型的深度训练通常受限于I/O，因此在训练和不确定性量化期间主动管理数据加载越来越受关注。那些基于对BDL后验的影响来量化和控制单个计算所提供信息的方法，在深度训练中作为算法数据处理的形式化方法显示出潜力（Tatzel等人，2023），它们使用概率数值线性代数（Wenger等人，2022）来选择数据上的稀疏信息性"视图"。

奇异学习理论。奇异学习理论（SLT；Watanabe，2009）利用非平衡统计力学的原理，研究贝叶斯损失（如边际对数似然的近似）与神经网络损失函数之间的关系。最近的研究将贝叶斯方法与奇异学习理论联系起来（Wei & Lau，2023）。

共形预测。对于不确定性量化，共形预测等替代方法已成为贝叶斯方法的竞争对手，并产生校准良好的不确定性（Vovk等人，2005）。深度学习模型可用于开发共形预测算法（Meister等人，2023），反之，共形预测方法可用于量化或校准深度学习模型中的不确定性。一种贝叶斯方法的共形预测已经开始出现（Hobbahn等人，2022；Murphy，2023），有望提供一种协同方法，将贝叶斯推理的优势与共形预测提供的良好校准的不确定性量化相结合。

大语言模型作为分布。大语言模型可以在任意复杂的程序和工作流中灵活地用作分布对象。通过采取贝叶斯立场，有几个问题值得探索。当多个大语言模型交互时，如何进行联合推断？什么是有效的方法来边缘化由大语言模型生成的潜在变量，从而促进对这些潜在空间的联合学习？是否有可能采用计算统计或近似推断的工具来与大语言模型进行各种形式的推理？是否存在创新方法，协同小型和大型大语言模型，以实时摊销推断？

元模型。当思考BDL是否会与语言模型的发展轨迹平行时，一个有趣的前景浮现出来。能否设想在BDL框架内开发一个贝叶斯元模型（Krueger等人，2017）？这个元模型，类似于语言模型，可以针对多个任务进行微调，并在这些任务上展示出有竞争力的预测性能，从而推广了摊销推断的方法（Garnelo等人，2018；Gordon等人，2019；Müller等人，2021）。

顺序决策基准。标准的图像基准只关注最先进的预测性能，非贝叶斯深度学习算法通常比贝叶斯深度学习（BDL）更有优势。为了量化预测不确定性，建议将注意力转向更全面的模拟研究或专注于顺序学习和决策的科学应用，例如实验设计、贝叶斯优化、主动学习或多臂赌博机。通过优先处理此类情境中的顺序问题，研究人员和从业者可以深入了解模型如何推广到新的未见数据、在不确定条件下的鲁棒性如何，以及决策者在现实场景中如何有效利用其不确定性估计。

# 5. 结语

本文表明，现代深度学习面临着各种持续的伦理、隐私和安全问题，尤其是在不同类型的数据、任务和性能指标的背景下。然而，其中许多问题可以在贝叶斯深度学习框架内解决，该框架建立在经历了两个半世纪科学和机器学习演变的基础原则之上。尽管仍存在一些技术挑战，但有一条清晰的路径，结合创造性和实用性来开发BDL方法，以适应21世纪数据、硬件和数值计算的进步，特别是在大规模基础模型的背景下。在未来，深度学习模型无缝集成到决策系统中，BDL因此成为更成熟AI的关键构建块，增加了额外的可靠性、安全性和信任层。

# 致谢

本研究部分得到麻省理工学院和哈佛大学布罗德研究所埃里克和温迪·施密特中心的支持（MS）。JA得到ANR-21-JSTM-0001资助。VF得到布兰科·韦斯奖学金的支持。PH衷心感谢德国研究联合会（DFG）卓越集群“机器学习——科学新视角”（EXC 2064/1，项目号390727645）的资助；德国联邦教育与研究部（BMBF）通过蒂宾根人工智能中心（FKZ：01IS18039A）的资助；以及巴登-符腾堡州科学、研究和艺术部的资助。JMHL感谢图灵人工智能奖学金（资助号EP/V023756/1）的支持。SM感谢国家科学基金会（NSF）的NSF CAREER奖（2047418）；NSF Grants 2003237和2007719；能源部科学办公室（资助号DE-SC0022331），以及迪士尼和高通的馈赠。CN衷心感谢EPSRC资助（EP/V022636/1和EP/Y028783/1）。AGW得到NSF CAREER IIS-2145492、NSF I-DISRE 193471、NSF IIS-1910266、BigHat Biosciences和Capital One的支持。

作者感谢ICML审稿人的评审和反馈。

# 影响声明

本文旨在推进机器学习领域的发展。这项工作有许多潜在的社会影响，作者认为没有需要在此特别强调的。

# A. 背景

本附录提供了支撑贝叶斯深度学习（BDL）的若干贝叶斯方法的背景知识。它可作为一份独立的入门教程，介绍贝叶斯方法论和BDL的基础。如需更详细的阐述，读者可参考本文提供的参考文献。

# A.1. 拉普拉斯近似

拉普拉斯近似是一种利用自动微分和数值线性代数，在神经网络输出上构建高斯过程（GP）后验的方法。考虑一个神经网络 $\mathbf{f}(\mathbf{x},\boldsymbol{\theta})$，它将输入 $\mathbf{x}$ 和参数 $\pmb{\theta}\in \mathbb{R}^{\nu}$（表示，例如，网络权重和偏置）映射到输出 $\mathbf{y}$。该神经网络经过训练，在监督训练数据集 $\mathcal{D} = (\mathbf{x}_i,\mathbf{y}_i)_{i = 1,\dots,n}$ 上找到能够最小化正则化经验风险函数 $\mathcal{L}(\pmb{\theta})$ 的参数 $\tilde{\pmb{\theta}}$。

$$
\tilde{\boldsymbol{\theta}} = \underset{\boldsymbol{\theta} \in \mathbb{R}^{\nu}}{\operatorname{argmin}} \mathcal{L}(\boldsymbol{\theta}) = \sum_{i=1}^{n} \ell(\mathbf{y}_i, \mathbf{f}(\mathbf{x}_i, \boldsymbol{\theta})) + r(\boldsymbol{\theta}),
$$

其中 $\ell$ 和 $r$ 分别是训练损失和正则化项。参数值 $\tilde{\theta}$ 通过与非贝叶斯深度学习相同的方法得到，即采用随机优化。可以解释通过训练神经网络得到的值 $\tilde{\theta}$。特别地，最小化 $\mathcal{L}$ 等价于最大化负 $\mathcal{L}$ 的指数，因为指数函数是严格递增的：

$$
\begin{array}{l} \tilde {\boldsymbol {\theta}} = \operatorname{argmax}_{\boldsymbol {\theta} \in \mathbb {R} ^ {\nu}} \exp (- \mathcal {L} (\boldsymbol {\theta})) \\ = \underset {\boldsymbol {\theta} \in \mathbb {R} ^ {\nu}} {\operatorname{argmax}} \left(\prod_ {i = 1} ^ {n} \exp (- \ell (\mathbf {y} _ {i}, \mathbf {f} (\mathbf {x} _ {i}, \boldsymbol {\theta}))) \exp (- r (\boldsymbol {\theta}))\right) \\ = \underset {\boldsymbol {\theta} \in \mathbb {R} ^ {\nu}} {\operatorname{argmax}} \prod_ {i = 1} ^ {n} p (\mathbf {y} _ {i} \mid \mathbf {f} (\mathbf {x} _ {i}, \boldsymbol {\theta})) p (\boldsymbol {\theta}) \\ = \operatorname{argmax}_{\boldsymbol {\theta} \in \mathbb {R} ^ {\nu}} p (\boldsymbol {\theta} \mid \mathcal {D}), \\ \end{array}
$$

其中 $\ell$ 被重新解释为负对数似然，$r$ 为负对数先验。这种解释对于深度学习中的常用选择是有效的。对数似然 $\ell$ 通常是指数族分布的对数。$r$ 的典型选择是 $l_{2}$ 损失的各种变体，例如参数的高斯先验的对数。

在此解释下，自动微分可用于计算 $\mathcal{L}$ 在 $\tilde{\pmb{\theta}}$ 附近的二阶泰勒展开，从而得到 $p(\pmb {\theta}\mid \mathcal{D})$ 的高斯近似：

$$
\log p (\boldsymbol {\theta} \mid \mathcal {D}) \approx \mathcal {L} (\tilde {\boldsymbol {\theta}}) + \frac {1}{2} (\boldsymbol {\theta} - \tilde {\boldsymbol {\theta}}) ^ {T} \boldsymbol {\Psi} (\boldsymbol {\theta} - \tilde {\boldsymbol {\theta}}) = \log \mathcal {N} (\boldsymbol {\theta}; \tilde {\boldsymbol {\theta}}, - \boldsymbol {\Psi} ^ {- 1}). \tag {1}
$$

$\Psi$ 名义上是 $\mathcal{L}$ 的 Hessian 矩阵。由于其关于 $\nu$ 的二次依赖，通常使用其近似。特别重要的是广义高斯-牛顿（GGN）矩阵 $\mathbf{G}$ (Schraudolph等，2007; Martens，2010)，

$$
\Psi \approx \mathbf {G} = \sum_ {i = 1} ^ {n} \mathbf {J} _ {\tilde {\boldsymbol {\theta}}} (\mathbf {x} _ {i}) \left(\nabla_ {\mathbf {f}} \nabla_ {\mathbf {f}} ^ {T} \ell (\mathbf {y} _ {i}, \mathbf {f} (\mathbf {x} _ {i}, \tilde {\boldsymbol {\theta}}))\right) \mathbf {J} _ {\tilde {\boldsymbol {\theta}}} ^ {T} (\mathbf {x} _ {i}) + \nabla \nabla^ {T} r (\tilde {\boldsymbol {\theta}}), \tag {2}
$$

该矩阵可利用损失对 logit 输入的闭式 Hessian 矩阵以及神经网络 $\mathbf{f}$ 的雅可比矩阵

$$
\left[ \mathbf {J} _ {\tilde {\boldsymbol {\theta}}} (\mathbf {x} _ {i}) \right] _ {a, b} = \left. \frac {\partial f _ {b} (\mathbf {x} _ {i} , \boldsymbol {\theta})}{\partial \theta_ {a}} \right| _ {\boldsymbol {\theta} = \tilde {\boldsymbol {\theta}}}
$$

来评估。该矩阵具有低秩性，可进行高效操作，例如计算方程 (2) 中所需的逆。为了将 $\theta$ 上的这种近似信念传播到 $\mathbf{f}$ 的输出，通常将网络在 $\tilde{\theta}$ 附近对 $\theta$ 进行线性化：

$$
\mathbf {f} (\mathbf {x}, \boldsymbol {\theta}) \approx \mathbf {f} (\mathbf {x}, \tilde {\boldsymbol {\theta}}) + (\boldsymbol {\theta} - \tilde {\boldsymbol {\theta}}) ^ {T} \mathbf {J} _ {\tilde {\boldsymbol {\theta}}} (\mathbf {x}).
$$

注意，该近似是关于 $\theta$ 的；神经网络对其输入 $\mathbf{x}$ 仍是非线性函数。

在此线性化下，与方程 (1) 中 $\theta$ 的高斯后验相关联的 $\mathbf{f}(\mathbf{x})$ 上的后验是一个高斯过程：

$$
p (\mathbf {f} (\mathbf {x}) \mid \mathcal {D}) \approx \mathcal {G P} \left(\mathbf {f} (\cdot), \mathbf {f} (\mathbf {x}, \tilde {\boldsymbol {\theta}}), - \mathbf {J} _ {\tilde {\boldsymbol {\theta}}} (\cdot) \boldsymbol {\Psi} ^ {- 1} \mathbf {J} _ {\tilde {\boldsymbol {\theta}}} (\cdot)\right).
$$

该高斯过程的均值函数对应于非贝叶斯深度学习中使用的训练后的神经网络 $\mathbf{f}(\cdot, \tilde{\boldsymbol{\theta}})$。其核是神经正切核的后验版本 (Jacot等，2018)。这种具体的实践联系使得拉普拉斯近似能够作为深度学习的即插即用方法使用；神经网络被训练或使用预训练的网络。随后计算 GGN 矩阵和雅可比矩阵。训练后的神经网络则作为点估计保留，现在作为 GP 的后验均值，并辅以结构化的 GP 不确定性。训练时的计算开销仅限于数值线性代数，其成本与训练集规模 $n$ 和参数空间维度 $\nu$ 呈线性关系。测试时，对给定输入 $\mathbf{x}'$ 的推断需要一次反向传播来计算雅可比矩阵 $\mathbf{J}_{\tilde{\boldsymbol{\theta}}}(\mathbf{x}')$，与计算 $\mathbf{f}(\mathbf{x}', \tilde{\boldsymbol{\theta}})$ 所需的前向传播相比，产生恒定的开销。

拉普拉斯近似的一个优势是能够以闭式形式计算近似后验的边缘似然 (Immer等，2021a)，这可用于神经网络中的贝叶斯模型选择，例如用于不变性学习 (Immer等，2022b)、语言模型的语言探针 (Immer等，2022a) 或神经网络剪枝 (Dhahri等，2024)。因此，拉普拉斯近似使贝叶斯深度学习在计算上更为可行。

# A.2. 变分推断

变分推断是一种近似推断方法，旨在将后验推断视为变分优化问题，以避免精确推断的难处理性。考虑一些随机参数 $\Theta$、数据 $\mathcal{D}$、似然函数 $p(\mathcal{D} \mid \boldsymbol{\theta})$、先验 $p(\boldsymbol{\theta})$ 以及由下式给出的后验 $p(\boldsymbol{\theta} \mid \mathcal{D})$：

$$
p (\pmb {\theta} \mid \mathcal {D}) = \frac {p (\mathcal {D} \mid \pmb {\theta}) p (\pmb {\theta})}{p (\mathcal {D})}.
$$

变分推断通过求解变分问题

$$
\min _ {q _ {\boldsymbol {\Theta}} (\boldsymbol {\theta}) \in \mathcal {Q} _ {\boldsymbol {\Theta}}} \mathbb {D} _ {\mathrm {K L}} \left(q _ {\boldsymbol {\Theta}} \middle\| p _ {\boldsymbol {\theta} \mid \mathcal {D}}\right) \tag {3}
$$

来近似 $p(\pmb{\theta} \mid \mathcal{D})$，其中 $q(\pmb{\theta})$ 是某个变分分布族 $\mathcal{Q}_{\Theta}$ 中的变分分布 (Wainwright & Jordan，2008)。在表达式 (3) 中，$\mathbb{D}_{\mathrm{KL}}$ 表示库尔贝克-莱布勒（KL）散度。由于后验 $p(\pmb{\theta} \mid \mathcal{D})$ 是被近似的分布，因此无法直接求解表达式 (3) 描述的变分问题。然而，可以证明求解该变分问题在数学上等价于最大化变分目标

$$
\mathcal {F} (q (\boldsymbol {\theta})) = \mathbb {E} _ {q (\boldsymbol {\theta})} [ \log p (\mathcal {D} \mid \boldsymbol {\theta}) ] - \mathbb {D} _ {\mathrm {K L}} (q _ {\boldsymbol {\Theta}} \| p _ {\boldsymbol {\Theta}})
$$

相对于变分分布 $q_{\Theta}(\pmb {\theta})\in \mathcal{Q}_{\Theta}$。换言之，

$$
\min _ {q _ {\boldsymbol {\Theta}} (\boldsymbol {\theta}) \in \mathcal {Q} _ {\boldsymbol {\Theta}}} \mathbb {D} _ {\mathrm {K L}} (q _ {\boldsymbol {\Theta}} \| p _ {\boldsymbol {\theta} \mid \mathcal {D}}) \Longleftrightarrow \max _ {q _ {\boldsymbol {\Theta}} (\boldsymbol {\theta}) \in \mathcal {Q} _ {\boldsymbol {\Theta}}} \mathcal {F} (q (\boldsymbol {\theta})).
$$

变分目标 $\mathcal{F}(q(\pmb{\theta}))$ 通常被称为证据下界（ELBO），因为可以证明

$$
\log p (\mathcal {D}) = \mathcal {F} (q (\boldsymbol {\theta})) + \mathbb {D} _ {\mathrm {K L}} \left(q _ {\boldsymbol {\Theta}} \middle\| p _ {\boldsymbol {\theta} \mid \mathcal {D}}\right),
$$

由于 KL 散度的非负性，这意味着 $\log p(\mathcal{D}) \geq \mathcal{F}(q(\pmb {\theta}))$。因此，变分目标是证据（即对数边缘似然 $\log p(\mathcal{D})$）的下界。最后，注意当且仅当 $q(\pmb {\theta}) = p(\pmb {\theta}\mid \mathcal{D})$ 时 $\log p(\mathcal{D}) = \mathcal{F}(q(\pmb {\theta}))$，这意味着当且仅当变分分布等于后验时，ELBO 才完全紧致。

一般而言，变分推断不能保证收敛到后验 $p(\pmb{\theta} \mid \mathcal{D})$，除非变分目标关于变分参数是凸的，并且后验是变分流形族 $\mathcal{Q}_{\Theta}$ 的成员，即 $p(\pmb{\theta} \mid \mathcal{D}) \in \mathcal{Q}_{\Theta}$。已经发展出多种近似推断方法来求解表达式 (3) 描述的变分问题。这些方法对变分流形族 $\mathcal{Q}_{\Theta}$ 做出不同假设，因此产生不同的后验近似。

对于神经网络的变分推断，两种成熟的方法是蒙特卡洛dropout（Gal & Ghahramani, 2016）和高斯均场变分推断（也被称为Bayes-by-backprop；Blundell等人，2015b；Graves，2011）。这些方法适用于基于随机小批量的变分推断，并且可以扩展到大型神经网络（Hoffman等人，2013）。最近关于贝叶斯神经网络（BNN）中函数空间变分推断（FSVI；Sun等人，2019；Rudner等人，2022a;b）的工作，将变分推断视为对诱导函数的优化，即：

$$
\min  _ {q _ {\mathbf {F}} (\mathbf {f}) \in \mathcal {Q} _ {\mathbf {F}}} \mathbb {D} _ {\mathrm {K L}} (q _ {\mathbf {F}} | | p _ {\mathbf {F} | \mathcal {D}})
$$

对于

$$
p (\mathbf {f} \mid \mathcal {D}) = \frac {p (\mathcal {D} \mid \mathbf {f}) p (\mathbf {f})}{p (\mathcal {D})}
$$

并带有适当定义的函数先验分布 $p(\mathbf{f})$。FSVI已被证明在计算机视觉任务中能够产生最先进的预测不确定性估计（Rudner等人，2022a）。

# A.3. 集成

深度集成指的是一种过程，其中神经网络架构使用不同的初始化多次重新训练，以找到不同的参数设置，然后在测试时对这些参数设置下的预测分布进行平均（Lakshminarayanan等人，2017）。在实践中，深度集成通过捕捉模型预测中的变异性，提供了一种表示认知不确定性的简单方法。这种方法与更传统的涉及从后验分布采样的贝叶斯方法形成对比。尽管作为近似推断过程而言并不传统，但深度集成通常比许多传统的深度学习近似推断方法（如使用高斯近似后验的变分推断）能更接近真实的后验预测分布（Wilson & Izmailov，2020；Izmailov等人，2021b）。

具体来说，对于不同的初始化，最小化标准损失，这通常等价于最小化负对数后验 $\log p(\pmb{\theta} \mid \mathcal{D})$，以得到

$$
\tilde {\pmb {\theta}} = \underset {\pmb {\theta} \in \mathbb {R} ^ {\nu}} {\mathrm {a r g m i n}} \mathcal {L} (\pmb {\theta}) = \underset {\pmb {\theta} \in \mathbb {R} ^ {\nu}} {\mathrm {a r g m i n}} \left(- \log p (\pmb {\theta} \mid \mathcal {D})\right) = \underset {\pmb {\theta} \in \mathbb {R} ^ {\nu}} {\mathrm {a r g m i n}} \left(- \log p (\mathcal {D} \mid \pmb {\theta}) - \log p (\pmb {\theta})\right),
$$

其中 $\theta \in \mathbb{R}^{\nu}$ 是神经网络参数，$\mathcal{D}$ 表示训练数据集。负对数似然 $-\log p(\mathcal{D}|\boldsymbol{\theta})$ 可能对应交叉熵损失，而高斯先验 $-\log p(\theta)$ 对应标准的 $\ell_2$ 正则化或权重衰减。在从不同初始化找到不同的局部解 $\tilde{\theta}_1,\dots ,\tilde{\theta}_s$ 后，对预测分布进行平均，以对测试输入 $x^{\prime}$ 进行预测：

$$
p (\mathbf {y} \mid \mathbf {x} ^ {\prime}, \mathcal {D}) = \frac {1}{s} \sum_ {i = 1} ^ {s} p (\mathbf {y} \mid \mathbf {x} ^ {\prime}, \tilde {\boldsymbol {\theta}} _ {i}). \tag {4}
$$

最初，测试时神经网络集成的过程并没有被纳入概率框架，并且经常被描述为拉普拉斯近似等标准近似推断方法的‘非贝叶斯’替代方案。然而，等式（4）可以被视为近似真实的后验预测分布

$$
p (\mathbf {y} \mid \mathbf {x} ^ {\prime}, \mathcal {D}) = \int p (\mathbf {y} \mid \mathbf {x} ^ {\prime}, \boldsymbol {\theta}) p (\boldsymbol {\theta} \mid \mathcal {D}) d \boldsymbol {\theta}. \tag {5}
$$

对于这个预测分布，有不同的解释方式。一些工作探索了贝叶斯推断与深度集成之间的联系（Ciosek等人，2020；Gustafsson等人，2020；He等人，2020；Pearce等人，2020；Wilson & Izmailov，2020；Izmailov等人，2021b；D'Angelo & Fortuin，2021；D'Angelo等人，2021）。一种解释将等式（4）视为等式（5）的蒙特卡洛近似，其中参数后验被表示为一组以不同模式为中心的点质量，这些点可以被视为近似的后验样本。然而，这种解释并非最有洞察力。

更有启发性的是将近似推断视为精确近似等式（5）中积分的任务。从这个角度来看，重点不在于收集后验样本。在固定的计算预算下，基于精确后验样本的预测分布值的蒙特卡洛平均，相对于其他替代方案，可能无法很好地近似该积分。一种更有说服力的数值积分方法是选择代表后验中典型点的参数值，这些点指示具有显著后验概率质量的区域，并且在测试集上产生多样化的预测。实现这一目标的一种启发式方法是选择对应于不同后验模式的点，正如深度集成所做的那样（Wilson & Izmailov，2020）。在实践中，与单个模式附近的样本（例如从变分高斯后验近似中得到的样本）相比，不同后验模式之间存在更多的函数变异性。

这些观察在实践中得到了实验的证实。深度集成往往比传统的单峰后验近似（Izmailov等人，2021b）更接近由穷尽式哈密顿蒙特卡洛（HMC）采样所表示的后验预测分布。深度集成的成功表明，更接近后验预测分布可以带来更好的预测性能，突出了进一步研究的潜力。有许多自然的方法可以近似后验预测分布。一个明显的方法是使用以多个后验模式为中心的高斯混合，而不是点质量的混合。这种方法在NeurIPS 2021近似贝叶斯推断竞赛中被发现能更紧密地近似后验预测分布并实现更好的预测性能（Wilson & Izmailov，2020；Wilson等人，2022；Shen等人，2024）。

从这些发现中得出的更一般的经验教训是，将一种方法是否‘贝叶斯’视为二元划分通常是不合理的；不同的近似推断过程落在一个谱系上，代表它们接近真实后验预测分布的程度。不同的方法根据模型和数据提供更好或更差的近似。在参数后验是单峰的情况下，深度集成作为推断过程用处不大。另一方面，如果存在许多模式，并且这些模式对应于做出不同预测的函数，那么深度集成作为近似贝叶斯推断过程是合理的，特别是在计算约束下，当无法表示许多不同的参数设置时。$^{1}$

# A.4. 后验采样算法

采样算法，特别是马尔可夫链蒙特卡洛（MCMC）方法，被广泛用于贝叶斯后验推断。这些算法通过构建一个马尔可夫链来工作，该链的平衡分布与所需（目标）分布匹配。通过实现马尔可夫链来更新参数，在进行了足够多的更新后，可以得到目标分布的样本。给定数据集 $\mathcal{D}$，参数为 $\pmb{\theta} \in \mathbb{R}^{\nu}$ 的模型，以及先验 $p(\pmb{\theta})$，目标是采样目标后验分布 $p(\pmb{\theta} \mid \mathcal{D}) \propto \exp(-U(\pmb{\theta}))$，其中能量函数为

$$
U (\boldsymbol {\theta}) = - \sum_ {\mathbf {x} \in \mathcal {D}} \log p (\mathbf {x} \mid \boldsymbol {\theta}) - \log p (\boldsymbol {\theta}).
$$

模拟以下连续时间随机微分方程（SDE）产生的样本以 $p(\pmb{\theta} \mid \mathcal{D})$ 为其平稳分布：

$$
\mathrm {d} \boldsymbol {\theta} = - \nabla U (\boldsymbol {\theta} _ {t}) \mathrm {d} t + 2 \mathrm {d} B _ {t}. \tag {6}
$$

$\nabla U(\pmb{\theta})$ 是 SDE 的漂移项，引导生成的样本趋向后验分布，而 $B_{t}$ 是布朗运动，为过程引入随机性。等式（6）中的 SDE 也被称为朗之万扩散方程，并作为许多蒙特卡洛采样算法的基础（Nemeth & Fearnhead，2021）。如果在短时间间隔 $\alpha > 0$ 上考虑朗之万扩散方程，则可以通过欧拉-丸山近似推导出其离散时间版本：

$$
\boldsymbol {\theta} _ {k + 1} = \boldsymbol {\theta} _ {k} - \alpha \nabla U (\boldsymbol {\theta} _ {k}) + \sqrt {2 \alpha} \boldsymbol {\xi} _ {k + 1}, \tag {7}
$$

其中 $\alpha > 0$ 是步长参数，$\xi$ 是标准高斯噪声。这种离散时间算法被称为未调整朗之万算法（unadjusted Langevin algorithm），或称朗之万蒙特卡洛算法（Langevin Monte Carlo algorithm）。然而，与连续时间的朗之万扩散方程不同，离散时间的未调整朗之万算法并非以 $p(\boldsymbol{\theta} \mid \mathcal{D})$ 作为其平稳分布来模拟样本，而是生成仅近似服从 $p(\boldsymbol{\theta} \mid \mathcal{D})$ 的样本。SDE 的离散化会导致后验样本出现偏差，减小步长参数 $\alpha$ 可以降低这种偏差。

对于大型数据集，未调整朗之万算法 (7) 在计算 $\nabla U(\pmb{\theta})$ 时需要遍历整个数据集求和，因此计算开销可能很大。随机梯度朗之万动力学（SGLD；Welling & Teh, 2011）通过使用随机梯度估计器 $\nabla \tilde{U}$（基于数据集 $\mathcal{D}$ 子集的 $\nabla U$ 的无偏估计器）来降低计算成本。SGLD 开创了随机梯度 MCMC（SG-MCMC）算法的一系列研究工作。它在第 $(k + 1)$ 步根据下式更新参数向量 $\pmb{\theta}$：

$$
\boldsymbol {\theta} _ {k + 1} = \boldsymbol {\theta} _ {k} - \alpha \nabla \tilde {U} (\boldsymbol {\theta} _ {k}) + \sqrt {2 \alpha} \boldsymbol {\xi} _ {k + 1}.
$$

SGLD 与随机梯度下降（SGD）之间的关键区别在于，SGLD 的每一步都添加了高斯噪声，这使其能够刻画完整的参数后验分布，而非收敛到单个点。

其他值得注意的 SG-MCMC 变体包括：随机梯度 HMC（SG-HMC；Chen et al., 2014），它利用辅助动量变量加速收敛；以及循环 SG-MCMC（Zhang et al., 2020b），它采用循环步长调度以有效探索参数后验分布的多个模态。此外，也有研究通过使用梅特罗波利斯调整（Metropolis adjustments）来减轻 SG-MCMC 方法的偏差（Zhang et al., 2020a；Garriga-Alonso & Fortuin, 2021）。

# A.5. 先验规范

统计模型 $\mathcal{M}$ 的参数向量 $\pmb{\theta} \in \mathbb{R}^{\nu}$ 上的先验 $p(\pmb{\theta} \mid \mathcal{M})$ 的规范一直是贝叶斯分析的核心部分，它允许将现有的领域知识或专家意见纳入统计推断。如果一个先验反映了此类知识，则称之为信息性先验（informative prior）。信息性先验的具体边界情况包括：强信息性先验（strongly informative prior），它主导来自观测数据（似然）的信息；以及弱信息性先验（weakly informative prior），它以一种模糊的方式与现有知识保持一致，使得后验被正则化为既基于数据又基于先验知识。在某些情况下，先验知识不存在，或者建模者不想依赖主观知识。此时，会使用无信息先验（uninformative prior）或客观先验（objective prior），常见选择是在参数上使用近乎平坦甚至均匀的先验分布。另一个值得提及的客观先验是参考先验（reference prior），其构造旨在最大化后验与所选先验之间的某种距离或散度。最后，在现代应用中，通常选择先验以将某些期望属性（如正则化或稀疏性）纳入模型。本文中的模型 $\mathcal{M}$ 被视为一个 BNN。然而，下面讨论的先验最常见于其他统计模型，然后通常被用于 BDL。

一种常见的方法是为 BNN 参数 $\theta$ 指定独立同分布（i.i.d.）的先验。更具体地说，一个常见的默认选择是使用零均值各向同性高斯先验：

$$
p (\boldsymbol {\theta} \mid \mathcal {M}) = \prod_ {i = 1} ^ {\nu} \mathcal {N} \left(\theta_ {i}; 0, \sigma^ {2}\right),
$$

这对应于最大后验（MAP）解意义上的 $l_{2}$ 正则化，其中 $\lambda = 1 / (2\sigma^2)$。因此，先验方差越大，引入的正则化越少，反之亦然。结合特定的激活函数（例如逻辑函数，它在 0 附近近似线性），选择较小的 $\sigma^2$ 会导致神经元及其组合的行为更接近线性，而较大的 $\sigma^2$ 则允许更多的非线性行为。因此，大多数情况下，选择标准高斯先验的流行方法并不令人满意，可能导致模型设定错误。这反过来可能引起冷后验效应（cold posterior effect），该效应在线性模型中已知存在（Grunwald & Van Ommen, 2017），在 BNN 中也被观测到（Wenzel et al., 2020; Fortuin et al., 2022; Nabarro et al., 2022）。对于特定问题，可以通过超参数调优或经验贝叶斯方法选择 $\sigma^2$。此外，可以将调优后的 $\sigma^2$ 直接迁移到某些架构（或者等价地，将频率派神经网络的 $\lambda$ 直接迁移）。另一种方法是对 $\sigma^2$ 施加逆伽马超先验，例如 $\sigma^2 \sim \Gamma^{-1}(\alpha, \beta)$，参见 Lampinen & Vehtari (2001)。为了纳入参数之间的先验依赖关系，可以将 i.i.d. 高斯先验扩展为具有零均值向量和协方差矩阵 $\Sigma$ 的多元正态分布，即：

$$
p (\boldsymbol {\theta} \mid \mathcal {M}) = \mathcal {N} _ {\nu} (\boldsymbol {\theta}; \mathbf {0}, \boldsymbol {\Sigma}),
$$

并可能对 $\pmb{\Sigma}$ 使用逆威沙特超先验。与 i.i.d. 高斯先验类似，也可以使用独立的拉普拉斯先验，即：

$$
p (\boldsymbol {\theta} \mid \mathcal {M}) = \prod_ {i = 1} ^ {\nu} \operatorname {L a p l a c e} \left(\theta_ {i}; 0, b\right),
$$

这在 MAP 意义上对应于 $\lambda = b^{-1}$ 的 $l_{1}$ 正则化（Williams, 1995）。选择尺度参数 $b$ 的方式与高斯先验中选择 $\sigma^2$ 的方式类似。此外，在 BNN 的背景下也使用了学生 t 先验（Neklyudov et al., 2018）。重尾先验在冷后验效应意义上可能对模型设定错误更具鲁棒性（Fortuin et al., 2022）。

另一个常被整合到 BNN 中的理想属性是稀疏性。高斯混合在这一背景下很受欢迎，包括高斯尺度混合先验（Blundell et al., 2015a）：

$$
p (\boldsymbol {\theta} \mid \mathcal {M}) = \prod_ {i = 1} ^ {\nu} \left(\pi \mathcal {N} \left(\theta_ {i}; 0, \sigma_ {1} ^ {2}\right) + (1 - \pi) \mathcal {N} \left(\theta_ {i}; 0, \sigma_ {2} ^ {2}\right)\right),
$$

其中 $\sigma_1^2 > \sigma_2^2$ 且 $\sigma_2^2 \ll 1$。类似地，也可以使用马蹄铁先验（horseshoe priors）（Carvalho et al., 2009）：

$$
p (\boldsymbol {\theta} \mid \mathcal {M}) = \prod_ {i = 1} ^ {\nu} \mathcal {N} (\theta_ {i}; 0, \sigma^ {2} \tau_ {i} ^ {2}),
$$

其中 $\tau_{i}$ 是局部收缩参数，具有半柯西超先验 $\tau_{i} \sim \mathbf{C}^{+}(0,1)$，而 $\sigma$ 是全局收缩参数。最后，另一个诱导稀疏性的先验是（非正常）对数均匀先验（Molchanov et al., 2017）：

$$
p (\boldsymbol {\theta} \mid \mathcal {M}) = \prod_ {i = 1} ^ {\nu} \operatorname {L o g} \mathrm {U} _ {\infty} \left(\theta_ {i}\right) \propto \prod_ {i = 1} ^ {\nu} \frac {1}{\theta_ {i}},
$$

以及它的正常对应形式（Neklyudov et al., 2017）：

$$
p (\boldsymbol {\theta} \mid \mathcal {M}) \propto \prod_ {i = 1} ^ {\nu} \operatorname {L o g} \mathrm {U} _ {\infty} \left(\theta_ {i}\right) \mathrm {I} _ {[ a, b ]} \left(\log \theta_ {i}\right).
$$

一些基于方向统计的先验已被探索用于 BNN（Sunde, 2023），但尚未得到广泛采用。同样，杰弗里斯先验（Jeffreys priors）（Ibrahim & Laud, 1991）在此背景下也未被广泛使用。尽管 Zellner 的 g-先验（Zellner, 1986）和 g-先验混合（Li & Clyde, 2018）在线性模型中非常流行，但它们最近才在 BDL 中引起关注（Antorán et al., 2022）。

在贝叶斯统计中，模型不确定性已被广泛研究了几十年（Hoeting et al., 1998; 1999; Wasserman, 2000）。在该框架内，不是使用单一模型 $\mathcal{M}$，而是考虑来自模型空间 $\mathbb{M}$ 的多个 BNN 架构 $\{\mathcal{M}_1,\dots ,\mathcal{M}_t\}$，同时利用 $p(\boldsymbol {\theta}\mid \mathcal{M})$ 和 $p(\mathcal{M})$。最近的研究集中于由不同权重包含模式定义的模型空间 $\mathbb{M}$ 上的模型不确定性（Hubin & Storvik, 2019; Skaaret-Lund et al., 2023），导致 $\mathbb{M}$ 中包含 $2^{\nu}$ 个模型。这需要额外的模型先验。如果假设模型 $\mathcal{M} = (\gamma_1,\ldots ,\gamma_\nu)$ 其中 $\gamma_{i}\in \{0,1\}$，$i\in \{1,\dots ,\nu \}$，则 Hubin & Storvik (2019) 和 Skaaret-Lund et al. (2023) 提出：

$$
p (\mathcal {M}) = \prod_ {i = 1} ^ {\nu} \operatorname {B e r n o u l l i} \left(\gamma_ {i}; \rho_ {i}\right),
$$

其中 $\rho_{i}$ 是特定权重的先验包含概率。类似地，Hubin & Storvik (2024) 提出使用：

$$
p (\mathcal {M}) \propto \prod_ {i = 1} ^ {\nu} \operatorname {B e t a B i n o m i a l} \left(\gamma_ {i}; 1, a _ {i}, b _ {i}\right).
$$

这两种先验在贝叶斯模型平均文献中很常见（Hoeting et al., 1999; Corani & Mignatti, 2015）。然而，更高级的模型先验，例如通过狄利克雷过程超先验（Grün & Hofmarcher, 2021）或稀释先验（George, 2010）来整合参数包含之间的依赖关系，尚未在贝叶斯深度学习背景下进行研究。同样值得注意的是，对于模型先验，输入层特定协变量的包含概率可由专家根据先验知识进行调整，从而允许将领域特定信息纳入贝叶斯神经网络的推断中。

将先验知识直接纳入参数先验通常是一个挑战。然而，神经网络概率建模的最新进展表明，纳入先验知识是可能的。一种方法涉及利用辅助目标来创建数据驱动的先验（Lopez et al., 2023; Rudner et al., 2023; 2024a; Sam et al., 2024）。另一种为神经网络指定有意义的先验的方法是采用函数空间视角。在这种方法中，贝叶斯神经网络在从参数先验采样时会生成一个函数上的分布$p(\mathbf{f})$。然后可以假设一个函数先验，例如高斯过程$p(\mathbf{f}) = \mathcal{GP}(\boldsymbol{\mu}(\cdot), \mathbf{K}(\cdot, \cdot))$，用于函数空间输出，从而允许纳入关于特定感兴趣现象的均值和协方差函数的专家知识。然而，直接应用这种函数先验可能会出现问题，因为高斯过程的支持集与贝叶斯神经网络的输出可能存在不匹配；参见Burt et al.（2020）；Rudner et al.（2022a）。出于同样的原因，使用KL散度来预训练参数上的先验以匹配所选的高斯过程先验是有问题的。Rudner et al.（2022a）通过考虑函数上分布之间的KL散度（这些分布通过设计是彼此绝对连续的）解决了这个问题。Tran et al.（2022a）也通过使用1-Wasserstein距离代替KL散度来学习权重空间中与所选高斯过程先验匹配的先验参数，解决了这一挑战。

本节仅对贝叶斯神经网络先验的广泛文献进行了简要概述。如需更全面的理解和相对较新的综述，读者可参考Fortuin（2022）。

# A.6. 深度核过程

深度核过程（DKP；Aitchison et al., 2021）是一种贝叶斯模型，它在核表示的深度序列上放置先验。这与其他深度贝叶斯模型（如深度高斯过程（DGP；Damianou & Lawrence, 2013）或贝叶斯神经网络（MacKay, 1995））相比是一种视角转变，后者在中间层特征或权重上放置先验。当核函数是各向同性时（如径向基函数和Matérn核），DKP与DGP等价。为了说明这一点，考虑一个具有各向同性核C的DGP，其中每一层被建模为以先前层为条件的多元高斯分布，

$$
\mathbf {F} _ {0} = \mathbf {X}, \tag {8a}
$$

$$
g \left(\mathbf {F} _ {j} \mid \mathbf {F} _ {j - 1}\right) = \prod_ {i = 1} ^ {r _ {j}} \mathcal {N} \left(\mathbf {f} _ {i, j}; \mathbf {0}, \mathbf {C} \left(\mathbf {F} _ {j}\right)\right), \tag {8b}
$$

$$
g \left(\mathbf {Y} \mid \mathbf {F} _ {\eta + 1}\right) = \prod_ {i = 1} ^ {r _ {j}} \mathcal {N} \left(\mathbf {y} _ {i}; \mathbf {f} _ {i, \eta + 1}, \sigma^ {2} \mathbf {I}\right). \tag {8c}
$$

此处，$\mathbf{F}_j \in \mathbb{R}^{n \times r_j}$ 是每个中间层 $j \in \{1, \dots, \eta\}$ 的特征表示，$\mathbf{X} \in \mathbb{R}^{n \times r_0}$ 是输入，$\mathbf{Y} \in \mathbb{R}^{n \times \rho_{\eta+1}}$ 是标签，$n$ 是数据点的数量。下标 $i$ 表示单个特征，因此 $\mathbf{f}_{i,j} \in \mathbb{R}^n$ 是第 $j$ 层的第 $i$ 个特征，$\mathbf{y}_i \in \mathbb{R}^n$ 是所有数据点的第 $i$ 个输出。$r_j$ 是第 $j$ 层每个数据点的特征数量，即“第 $j$ 层的宽度”。要获得核过程，需要考虑协方差矩阵。因此，对于每一层，定义Gram矩阵 $\mathbf{G}_j = \mathbf{F}_j \mathbf{F}_j^T / r_j \in \mathbb{R}^{n \times n}$。由于 $\mathbf{G}_j$ 是协方差为 $\mathbf{C}(\mathbf{F}_j)$ 的独立同分布高斯样本的外积，它必须服从Wishart分布，

$$
g (\mathbf {G} _ {j} \mid \mathbf {F} _ {j - 1}) = \mathcal {W} (\mathbf {G} _ {j}; \mathbf {C} (\mathbf {F} _ {j - 1}) / r _ {j}, r _ {j}).
$$

此外，根据各向同性假设，存在一个关于Gram矩阵的函数 $\mathbf{K}(\cdot)$，使得 $\mathbf{K}(\mathbf{G}_j) = \mathbf{C}(\mathbf{F}_j)$；参见Aitchison et al.（2021）。能够用Gram矩阵定义核函数意味着可以将方程（8）中的DGP写成一个具有Wishart先验的DKP，

$$
g \left(\mathbf {G} _ {1} \mid \mathbf {X}\right) = \mathcal {W} \left(\mathbf {G} _ {1}; \mathbf {X X} ^ {T} / r _ {0}, r _ {0}\right), \tag {9a}
$$

$$
g \left(\mathbf {G} _ {j} \mid \mathbf {G} _ {j - 1}\right) = \mathcal {W} \left(\mathbf {G} _ {j}; \mathbf {K} \left(\mathbf {G} _ {j - 1}\right) / r _ {j}, r _ {j}\right), \tag {9b}
$$

$$
g \left(\mathbf {y} _ {i} \mid \mathbf {G} _ {\eta}\right) = \mathcal {N} \left(\mathbf {y} _ {i}; \mathbf {0}, \mathbf {K} \left(\mathbf {G} _ {\eta}\right) + \sigma^ {2} \mathbf {I}\right). \tag {9c}
$$

由于方程（9）在中间Gram矩阵表示上放置了Wishart先验，因此得到的被称为深度Wishart过程（DWP；Aitchison et al., 2021）。深度逆Wishart过程（DIWP；Aitchison et al., 2021）则使用核上的逆Wishart过程先验（Shah et al., 2014）来定义。

与其他深度贝叶斯模型类似，一般DKP的闭式推断是不可能的。Aitchison et al.（2021）、Ober & Aitchison（2021a）和Ober et al.（2023）为DWP和DIWP开发了Gram矩阵上的近似后验，以允许变分推断。然而，尽管使用了近似后验，训练DWP或DIWP的计算成本仍然相当高。这是因为参数数量随数据点数量$n$呈二次方缩放，而评估其近似后验的对数概率（评估ELBO所必需的）随$n$呈三次方缩放。为了解决这个可扩展性挑战，诱导点近似提供了一种解决方案。特别是，全局诱导点方法（Ober & Aitchison, 2021b）使得DKP的训练能够随数据点数量线性缩放。

通过使用诱导点方案，Ober et al.（2023）的经验证明，DwP的近似后验性能优于DGP的近似后验。Aitchison et al.（2021）认为，由于BNN和DGP的先验和后验高度多模态，因此预计DWP的性能更好。特别是，常见的BNN和DGP近似后验未能充分处理特征或权重的旋转和排列对称性。DKP规避了这一多模态问题，因为Gram矩阵本质上是避免这些对称性的；特征空间中的任意旋转或排列可以通过映射 $\mathbf{F} \mapsto \mathbf{F}\mathbf{U}$ 表示，其中 $\mathbf{U}$ 是酉矩阵，但相应的Gram矩阵在此变换下保持不变，因为 $\mathbf{G} = \mathbf{F}\mathbf{F}^T \mapsto (\mathbf{F}\mathbf{U})(\mathbf{F}\mathbf{U})^T = \mathbf{G}$。

# A.7. 深度核机器

深度核机器（DKM；Yang et al., 2023a）是DKP的无限宽度类比。它们具有实际优势，更容易实现且训练成本更低，同时也具有理论优势，因为它们可以与现有的无限宽度神经网络文献相关联。然而，DKM并非严格意义上的贝叶斯模型。通常，对DKP或DGP取无限宽度极限会得到神经网络高斯过程（NNGP；Lee et al., 2017；Agrawal et al., 2020）。无限宽度极限被谨慎地取定，以保留中间Gram表示的灵活性。

可以从方程（8）的DGP按如下方式获得DKM。考虑每个中间层 $j \in \{1, \dots, \eta\}$ 的特征的以下近似后验：

$$
h (\mathbf {F} _ {j}) = \prod_ {i = 1} ^ {r _ {j}} \mathcal {N} (\mathbf {f} _ {i, j}; \mathbf {0}, \mathbf {G} _ {j}).
$$

此外，考虑最后一层的标准GP近似后验：

$$
h \left(\mathbf {F} _ {\eta + 1}\right) = \prod_ {i = 1} ^ {r _ {\eta + 1}} \mathcal {N} \left(\mathbf {f} _ {i, \eta + 1}; \boldsymbol {\mu} _ {i}, \boldsymbol {\Sigma}\right).
$$

此处，$\mathbf{G}_1,\dots ,\mathbf{G}_{\eta},\pmb {\mu}_1,\dots ,\pmb{\mu}_{r_{\eta +1}}$ 和 $\boldsymbol{\Sigma}$ 是变分参数。尽管这个近似后验族可能看起来有限制性，但中间层部分在无限宽度极限下包含了真实后验；参见Yang et al.（2023a）的附录E。边际似然的下界可以通过ELBO获得

$$
\mathrm {E L B O} = \sum_ {i = 1} ^ {r _ {\eta + 1}} \left\{\mathbb {E} _ {h (\mathbf {F} _ {\eta + 1})} \left[ \log g (\mathbf {y} _ {i} \mid \mathbf {f} _ {i, \eta + 1}) \right] - \mathbb {D} _ {\mathrm {K L}} (h (\mathbf {f} _ {i, \eta + 1}) \mid | g (\mathbf {f} _ {i, \eta + 1} \mid \mathbf {F} _ {\eta})) \right\} - \sum_ {j = 1} ^ {\eta} \beta_ {j} r _ {j} \mathbb {D} _ {\mathrm {K L}} (h (\mathbf {f} _ {j}) \mid | g (\mathbf {f} _ {j} \mid \mathbf {F} _ {j - 1})),
$$

其中使用参数$\beta_{j}$进行退火。与DWP一样，假设各向同性核函数，这意味着$\mathbf{C}(\mathbf{F}_j) = \mathbf{K}(\mathbf{G}_j)$。当中间层通过令$r\to \infty$且$r_j = r\rho_j$变宽时，对$\mathbf{F}_j$的依赖消失。如果不进行退火（即$\beta_{j} = 1$），则得到以下目标函数：

$$
\frac {\mathrm {E L B O}}{r} \rightarrow - \sum_ {j = 1} ^ {\eta} \rho_ {j} \mathbb {D} _ {\mathrm {K L}} \left(\mathcal {N} (\mathbf {0}, \mathbf {G} _ {j}) \mid \mid \mathcal {N} (\mathbf {0}, \mathbf {K} (\mathbf {G} _ {j - 1}))\right). \tag {10}
$$

当$\mathbf{G}_j = \mathbf{K}(\mathbf{G}_{j - 1})$时，目标函数（10）最大化，这与相应的NNGP相同（Lee等人，2017；Agrawal等人，2020）。如果根据宽度进行退火，取$\beta_{j} = 1 / r$，则得到以下目标函数：

$$
\begin{array}{l} \mathrm {E L B O} \rightarrow \sum_ {i = 1} ^ {r _ {\eta + 1}} \mathbb {E} _ {h (\mathbf {F} _ {\eta + 1})} \left[ \log g (\mathbf {y} _ {i} \mid \mathbf {f} _ {i, \eta + 1}) \right] \\ - \sum_ {i = 1} ^ {r _ {\eta + 1}} \mathbb {D} _ {\mathrm {K L}} \left(\mathcal {N} \left(\boldsymbol {\mu} _ {i}, \boldsymbol {\Sigma}\right) \mid \mid \mathcal {N} (\mathbf {0}, \mathbf {K} \left(\mathbf {G} _ {\eta}\right)\right) \tag {11} \\ - \sum_ {j = 1} ^ {\eta} \rho_ {j} \mathbb {D} _ {\mathrm {K L}} (\mathcal {N} (\mathbf {0}, \mathbf {G} _ {j}) | | \mathcal {N} (\mathbf {0}, \mathbf {K} (\mathbf {G} _ {j - 1})) + \text {c o n s t a n t}. \\ \end{array}
$$

优化目标函数（11）的模型称为DKM，而（11）被称为DKM目标函数。在极限情况下，DKM目标函数不依赖于中间特征$\mathbf{F}_j$，这意味着DKM中学到的表示完全由确定性格拉姆矩阵$\mathbf{G}_1, \ldots, \mathbf{G}_\eta$描述。为了解释DKM目标函数，注意到似然项鼓励数据拟合，而KL散度则将模型正则化至NNGP（Lee等人，2017；Agrawal等人，2020）。DKM中表示学习的程度可以通过改变$\rho_j$参数来控制。相比之下，NNGP目标函数（10）中缺少似然项，阻止了NNGP中进行表示学习；中间格拉姆矩阵是固定的，仅依赖于输入数据。

与DKP目标函数类似，DKM目标函数在大数据集上优化时计算不可行，其复杂度与数据点数量呈三次方关系。然而，Yang等人（2023a）已经证明，若使用全局诱导点方法，DKM目标函数可以以线性复杂度进行优化。DKM已被扩展到卷积架构，在CIFAR-10上实现了几乎与神经网络相当的性能（Milsom等人，2023）。

# B. 诊断、度量和基准

目前，缺乏专门针对BDL需求的收敛性和性能度量。开发此类工具有助于识别BDL的目标并评估其进展。此外，评估指标、数据集和基准的选择在BDL社区中缺乏共识，这反映了在一个传统上通过频率论视角看待的领域中，尤其是关于测试数据性能方面，明确定义BDL目标的困难。许多通用的贝叶斯诊断和评估方法都是通过贝叶斯工作流提出的（Gelman等人，2020）。本附录讨论了与BDL最相关的方法。

参数空间的收敛诊断。SG-MCMC采样的收敛性和采样效率分析（Gelman等人，2013；Vehtari等人，2021）变得微妙，目前通过使用预测分布的汇总统计量对这些量进行相当简单的分析来绕过。更一般地说，在BDL模型的高维和多模态设置中验证推理算法的收敛性并非易事。为BNN设计的收敛性检查需要进一步研究。

预测空间的性能度量。BDL和GP文献通常关注预测分布的均值，忽略了预测分布的方差分析。一些性能指标常用于评估方差水平，例如通过评估测试数据预测的对数似然或熵（Rudner等人，2022a；2023）。然而，目前缺乏一种系统的方法来表征BDL推理中的预测不确定性（除了二分类问题中广泛使用的AUROC和AUPRC外）（Arbel等人，2023）。为评估认知不确定性和偶然不确定性设定指标的挑战减缓了BDL的进展，可以通过为BDL方法建立广泛接受的基准来潜在地解决。

错误设定场景下的性能度量。应对分布偏移和测试数据性能相关的挑战需要开发稳健的性能度量。为了在分布偏移下建立BDL模型的可靠性，更紧的泛化边界（例如PAC-Bayes框架提供的边界（Langford & Shawe-Taylor, 2002；Parrado-Hernandez等人，2012））对于获得模型性能的概率保证至关重要。此外，在错误设定的场景中，评估校准变得至关重要。创新技术，如两阶段校准（Guo等人，2017）和一致性预测（Papadopoulos等人，2007）或其贝叶斯对应物（Hobbahn等人，2022），通过分别细化预测概率和量化预测不确定性，提供了实用的解决方案。这些方法共同有助于在基本假设可能与真实数据分布不一致的场景中更全面地评估模型性能。

数据集的概率处理。将数据作为一等公民进行概率处理，并能够在BNN中进行推理，这似乎很有前景。这种概率方法可能有助于创建更集中、更有用的数据集，以表示海量数据源中包含的知识，从而提高训练和维护大型模型的能力。

# C. 软件可用性

将BDL方法应用于实际问题仍然比选择现成的标准深度学习解决方案更复杂，这限制了BDL在实际中的采用。软件开发是鼓励深度学习实践者使用贝叶斯方法的关键。更一般地说，需要开发使实践者更容易在其项目中尝试BDL的软件。BDL的使用必须在人力投入上与标准深度学习具有竞争力。

已经有一些努力在深度学习框架之上开发软件包、库或概率编程语言（PPL）。bayesianize（Ritter等人，2021）、bnn-priors（Fortuin等人，2021）、Laplace（Daxberger等人，2021a）、Pyro（Bingham等人，2019）和TyXe（Ritter & Karaletsos，2022）是基于PyTorch构建的软件种类，TensorFlow Probability是基于TensorFlow构建的库，Fortuna（Detommaso等人，2023）是基于JAX构建的库。概率编程社区的贡献将有助于取得进一步进展。

PPL，如Pyro，在简化概率推理应用于深度学习方面发挥作用。事实上，PPL中对NN的概率处理抽象（例如BDL库TyXe中执行的抽象）可以简化先验和推理技术对任意NN的应用，正如TyXe中实现的多种模型所展示的那样。将这些思想移植到涉及LLM和更定制化概率结构的现代问题设置中，将使得BDL能够在实际问题中使用。

当代深度学习在各个方面（数据集、参数空间、结构化函数值输出）推动着规模的极限。对于点估计，社区一直在开发以数组为中心的编程范式，允许分片、部分求值、延续等。BDL应该能够映射这些思想以开发类似的软件。

# D. 主题发展

本附录提供了BDL的未来发展主题或专业领域。这些包括用于人机交互的BDL、终身学习和去中心化学习、贝叶斯强化学习（RL）以及特定领域的BDL模型。

人机交互与可解释AI。使AI系统能够传达和解释其不确定性，可以建立信任并改善AI系统与人类之间的交互。尽管社区已经努力解释DNN的预测，但最近的工作旨在解释BDL方法的不确定性（Antoran等人，2021；Bhatt等人，2021）。理解哪些输入模式导致高预测不确定性可以建立对AI系统的信任，并提供关于数据稀疏的输入区域的见解。例如，在训练贷款违约预测器时，数据科学家可以识别训练数据中代表性不足的人口亚群体（按年龄、性别或种族）。从这些群体收集更多数据可以让更广泛的客户获得更准确的预测。

终身学习与去中心化学习。一个当代研究方向是超越“静态”训练-测试框架，专注于测试集未知的“动态”问题。这包括预测性能、鲁棒性和安全性很重要，且基础设施存在现实约束的情况。其中两个问题分别是终身学习和去中心化学习。关注这些问题有望带来贝叶斯思想对深度学习有用的新范式。

高效探索在强化学习中的应用。强化学习是贝叶斯深度学习展现潜力的领域之一。例如，汤普森采样作为一种常用的决策启发式方法，其原理是“根据动作成为最优的概率随机选择动作”（Russo et al., 2018）。汤普森采样在探索与利用之间取得平衡，其精确形式需要从贝叶斯后验分布中采样。实践中常采用近似方法，而近期研究表明，多测试输入上的多元联合预测分布的质量对决策至关重要（Wen et al., 2021; Osband et al., 2023）。这一点尤为重要，因为典型的贝叶斯和非贝叶斯方法通常通过评估单个测试输入的边际预测质量来衡量性能，而忽略了潜在的依赖关系（Osband et al., 2022）。尽管深度集成是捕获不确定性的常用基线方法，但基于最后一层拉普拉斯近似的贝叶斯深度学习方法在多元联合预测质量上可超越深度集成（Antoran et al., 2023）。如何在计算成本与多元联合预测质量之间取得平衡，开发相应方法，是未来研究需要进一步探索的方向（Osband et al., 2023）。另一个活跃的研究领域是强化学习与贝叶斯深度学习的交叉，旨在根据与环境交互的数据生成价值函数（例如Q函数）的精确后验近似（Janz et al., 2019）。这一设定不同于典型的贝叶斯监督学习，因为价值函数的输出无法直接观测，只能获得奖励信号。

计算机视觉领域。针对计算机视觉任务，贝叶斯深度学习方法已得到发展。例如，Kou等（2024）在扩散模型中采用贝叶斯深度学习构建像素级不确定性估计器用于图像生成。Goli等（2024）利用贝叶斯深度学习在计算机图形学中评估预训练神经辐射场的不确定性。未来计算机视觉领域的贝叶斯深度学习研究可聚焦于提升预测性能及进一步发展不确定性量化方法。计算机视觉与自然语言处理共同构成可能推动贝叶斯深度学习广泛应用的应用方向。

领域特定的贝叶斯深度学习模型。针对具体领域，结合数据特征与任务需求，开发与深度学习模型相结合的贝叶斯方法存在诸多机遇。这包括探索层次模型、迁移学习或元学习等策略。以分子性质预测为例，虽然存在多种数据集，但每个数据集的可用数据有限（Klarner et al., 2023）。可将学习分子特征表征的深度学习模型与接收这些表征作为输入的贝叶斯方法相结合。后者能够在数据有限的条件下为各个任务捕获不确定性并做出预测，而深度学习特征则在任务间共享。