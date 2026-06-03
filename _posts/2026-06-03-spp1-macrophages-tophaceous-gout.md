---
layout: post
title: "痛风石微环境中的 SPP1+ 巨噬细胞：从急性炎症到空间组织重塑"
date: 2026-06-03 15:00:00 +0800
categories: gout single-cell spatial-transcriptomics macrophage
---

<p><a href="/assets/pdfs/gout-study-note-2026-06-02.pdf">学习笔记 PDF 下载</a></p>

<div class="pdf-frame">
  <iframe src="/assets/pdfs/gout-study-note-2026-06-02.pdf" title="痛风学习笔记 PDF"></iframe>
</div>

## 参考文献

这篇学习笔记围绕痛风发病机制及痛风石微环境的研究脉络展开，重点参考以下文献：

1. Dalbeth N, et al. Gout. *Lancet*. 2021;397:1843-1855.
2. Leask MP, et al. The pathogenesis of gout: molecular insights from genetic, epigenomic and transcriptomic studies. *Nature Reviews Rheumatology*. 2024;20:510-523.
3. FitzGerald JD, et al. 2020 American College of Rheumatology Guideline for the Management of Gout. *Arthritis Care & Research*. 2020;72:744-760.
4. Deconstruction of tophi and synovium defines SPP1+ macrophages involved in extracellular matrix remodelling in gout. *Annals of the Rheumatic Diseases*. 2025. PMID: 41107120. DOI: [10.1016/j.ard.2025.09.003](https://doi.org/10.1016/j.ard.2025.09.003).

## 一、核心问题：痛风不只是“尿酸高”

痛风的传统解释通常从高尿酸血症出发：尿酸盐水平升高，单钠尿酸盐晶体（monosodium urate crystals, MSU crystals）在关节局部沉积，随后诱发急性炎症反应。这一框架能够很好地解释急性痛风发作，但对于慢性痛风石形成、关节局部破坏、纤维化和骨侵蚀等问题，仍然不够充分。

因此，当前研究的关键问题逐渐从“为什么尿酸升高”推进到“为什么某些关节形成持续性的病理微环境”。换言之，痛风不仅是系统性代谢异常，也是局部组织微环境被长期重塑后的结果。

## 二、经典机制：MSU 晶体驱动急性炎症

在急性痛风发作中，MSU 晶体是核心触发因素。巨噬细胞吞噬 MSU 晶体后，激活 NLRP3 inflammasome，继而促使 caspase-1 激活，导致 IL-1 beta 和 IL-18 等炎症因子释放，并伴随细胞焦亡。这一过程可概括为：

```text
MSU crystals
    ↓
macrophage phagocytosis
    ↓
NLRP3 inflammasome activation
    ↓
caspase-1 activation
    ↓
IL-1 beta release and pyroptosis
    ↓
acute gout flare
```

这一模型强调的是晶体与先天免疫之间的直接关系。它解释了急性炎症的快速启动，也构成了 IL-1 beta 相关治疗策略的理论基础。

## 三、从系统代谢到局部组织：研究问题的转向

痛风的上游基础是尿酸稳态失衡。SLC2A9、SLC22A12 和 ABCG2 等尿酸转运相关基因参与尿酸排泄和重吸收，影响个体高尿酸血症风险。GWAS 和遗传学研究在这一层面提供了系统性解释。

但高尿酸血症并不等同于所有关节都会发生同样程度的炎症和破坏。近年来的研究开始强调，关节局部微环境可能决定 MSU 晶体是否沉积、沉积后是否持续存在，以及是否进一步发展为慢性痛风石。

这一转向大致包括四个层次：

1. 软骨和 extracellular matrix（ECM）成分可能影响 MSU 晶体形成，并增强炎症细胞募集。
2. 受损关节本身可能形成一种易感局部生态位，解释痛风发生的部位偏好和复发倾向。
3. SRS 成像和滑膜类器官模型可以动态观察 MSU 晶体的时空沉积过程。
4. 单细胞和空间组学进一步解析痛风石内免疫细胞、基质细胞和骨相关细胞的空间组织方式。

因此，痛风研究的逻辑正在从“代谢异常导致晶体沉积”扩展为“晶体沉积诱导并维持局部组织生态位”。

## 四、单细胞和空间组学视角：痛风石是结构化病灶

痛风石并不是简单的尿酸盐堆积物，而是由 MSU 晶体、免疫细胞、成纤维细胞、血管结构、骨相关细胞和 ECM 共同组成的慢性病理结构。单细胞转录组和空间转录组的价值在于，它们能够把这一结构拆解为不同细胞状态和空间分区。

在相关研究中，作者通过单细胞转录组识别了多个免疫和基质细胞亚群，并结合空间分析和细胞通讯推断，进一步定位这些细胞在痛风石不同区域中的相互作用。这里的重点不是单纯“有哪些细胞”，而是“哪些细胞在什么位置、通过什么信号轴共同维持病灶结构”。

## 五、SPP1+ TGAMs：连接炎症与组织重塑的巨噬细胞状态

该研究的一个核心发现是 SPP1+ tophaceous gout-associated macrophages，即 SPP1+ TGAMs。这里的 “tophaceous gout” 指痛风石性痛风，也就是已经形成痛风石的慢性痛风状态。

SPP1+ TGAMs 表达 SPP1、MMP9、CHI3L1 等基因，提示其并非单纯急性炎症型巨噬细胞，而更接近一种慢性炎症和组织重塑相关的巨噬细胞状态。MMP9 指向基质降解和重塑，CHI3L1 常与炎症、纤维化和组织修复过程相关，而 SPP1 则可能介导免疫细胞与基质细胞之间的黏附、迁移和信号通讯。

因此，SPP1+ TGAMs 的意义在于：它们可能把 MSU 晶体诱导的炎症反应，与 ECM remodeling、纤维化、破骨细胞分化和关节结构破坏连接起来。

## 六、细胞通讯：SPP1-CD44 轴是关键连接

与间歇期痛风相比，痛风石性痛风中的细胞-细胞通讯明显增强。其中，SPP1-CD44 是一个突出的配体-受体互作轴。SPP1+ TGAMs 通过 SPP1 信号与成纤维细胞、成骨细胞谱系细胞、破骨细胞谱系细胞以及 Tregs 等细胞发生联系。

这一点非常关键。它提示巨噬细胞不只是炎症反应的执行者，而可能成为痛风石微环境的组织者。通过 SPP1-CD44 信号，巨噬细胞可以影响基质细胞活化、胶原沉积、骨重塑和免疫调节，从而推动痛风石从晶体沉积灶转变为稳定的慢性组织病灶。

## 七、空间分区：内层免疫-基质互作，外层结构重塑

空间分析进一步显示，痛风石内部存在区域化的信号分布。SPP1 signaling 更偏向于 corona zone，而 collagen signaling 更偏向于 fibrovascular zone。

可以把这一结构理解为两个相互衔接的层次：

```text
corona zone
    immune-stromal interaction
    SPP1-CD44 signaling
    macrophage-fibroblast / macrophage-bone-lineage crosstalk

fibrovascular zone
    collagen signaling
    ECM organization
    fibrosis and structural remodeling
```

这说明痛风石不是均质性炎症团块，而是具有空间分工的病理生态位：内层更偏向 SPP1 驱动的免疫-基质互作，外层更偏向 collagen 驱动的结构重塑。

## 八、整体疾病模型

基于上述证据，可以把痛风石形成和进展概括为以下逻辑链条：

```text
persistent hyperuricaemia
    ↓
MSU crystal deposition in joints
    ↓
local tophus microenvironment formation
    ↓
expansion of SPP1+ TGAMs
    ↓
SPP1-CD44 signaling activation
    ↓
crosstalk with fibroblasts, osteoblast-lineage cells,
osteoclast-lineage cells, and Tregs
    ↓
ECM remodeling, fibrosis, and osteoclast differentiation
    ↓
tophus maturation and joint damage
```

这一模型的重点是把系统性高尿酸、局部晶体沉积、巨噬细胞状态转变、细胞通讯和空间组织重塑放在同一条病理链上理解。

## 九、我的理解

这篇工作的价值不只是发现了一个 SPP1+ 巨噬细胞亚群，而是把痛风石重新定义为一个由免疫细胞、基质细胞和骨相关细胞共同构成的慢性空间微环境。相比急性痛风中“MSU-NLRP3-IL-1 beta”的线性炎症模型，痛风石性痛风更接近一种慢性组织生态位重塑过程。

从单细胞组学角度看，SPP1+ TGAMs 提供了一个细胞状态层面的切入点；从空间组学角度看，corona zone 和 fibrovascular zone 的信号分区解释了为什么痛风石能够形成相对稳定的结构；从疾病机制角度看，SPP1-CD44 轴可能是连接慢性炎症与 ECM remodeling 的关键桥梁。

## 十、可以继续追问的问题

1. SPP1+ TGAMs 是痛风石形成的驱动因素，还是痛风石成熟后的结果？
2. SPP1-CD44 轴是否具有治疗靶点价值？
3. 降尿酸治疗后，SPP1+ TGAMs 相关的微环境是否可逆？
4. 这种 macrophage-stromal remodeling 轴是否也存在于其他晶体相关或慢性炎症性关节病中？
5. GWAS 指向的系统性尿酸调控基因，如何与局部组织微环境中的细胞状态联系起来？

## 总结

这篇学习笔记的主线可以概括为：痛风研究正在从系统性尿酸代谢和急性炎症模型，走向局部组织微环境和空间生态位模型。MSU 晶体触发急性炎症，但慢性痛风石的形成需要进一步理解 SPP1+ TGAMs、SPP1-CD44 细胞通讯、ECM remodeling 和空间分区结构之间的关系。

因此，痛风石性痛风不应只被看作尿酸盐沉积的终末结果，而应被理解为一个由晶体、免疫细胞、基质细胞和骨相关细胞共同塑造的慢性组织重塑过程。
