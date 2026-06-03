---
layout: post
title: "Deconstruction of Tophi and Synovium Defines SPP1+ Macrophages Involved in Extracellular Matrix Remodelling in Gout"
date: 2026-06-03 15:00:00 +0800
categories: gout single-cell spatial-transcriptomics macrophage
---

<div class="pdf-frame">
  <iframe src="/assets/pdfs/gout-study-note-2026-06-02.pdf#toolbar=0&navpanes=0" title="Gout study note PDF preview"></iframe>
</div>

<div class="pdf-gate" data-pdf-gate data-pdf-path="/assets/pdfs/gout-study-note-2026-06-02.pdf" data-expected-hash="d235bcd0c966b18fa5304b4e9838a7a924acfcf034a5760ec1641ea3df547f09">
  <form class="pdf-gate-form">
    <label for="pdf-access-code">Access code for downloading the study note PDF</label>
    <div class="pdf-gate-row">
      <input id="pdf-access-code" name="access-code" type="password" autocomplete="off" placeholder="Enter access code">
      <button type="submit">Show Download Link</button>
    </div>
    <p class="pdf-gate-message" role="status"></p>
  </form>

  <div class="pdf-actions" hidden>
    <a href="/assets/pdfs/gout-study-note-2026-06-02.pdf">Download study note PDF</a>
  </div>
</div>

<script>
(() => {
  const gate = document.querySelector("[data-pdf-gate]");
  if (!gate || !window.crypto?.subtle) return;

  const form = gate.querySelector(".pdf-gate-form");
  const input = gate.querySelector("#pdf-access-code");
  const message = gate.querySelector(".pdf-gate-message");
  const actions = gate.querySelector(".pdf-actions");
  const storageKey = "gout-study-note-download-unlocked";

  const digest = async (value) => {
    const data = new TextEncoder().encode(value);
    const buffer = await crypto.subtle.digest("SHA-256", data);
    return [...new Uint8Array(buffer)]
      .map((byte) => byte.toString(16).padStart(2, "0"))
      .join("");
  };

  const unlock = () => {
    actions.hidden = false;
    form.hidden = true;
  };

  if (localStorage.getItem(storageKey) === gate.dataset.expectedHash) {
    unlock();
  }

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    const hash = await digest(input.value.trim());

    if (hash === gate.dataset.expectedHash) {
      localStorage.setItem(storageKey, hash);
      unlock();
      return;
    }

    message.textContent = "Incorrect access code.";
    input.value = "";
    input.focus();
  });
})();
</script>

## References

This study note summarizes the mechanistic background of gout and the emerging single-cell and spatial transcriptomic framework for understanding the gouty tophus microenvironment. The discussion is organized around the following references:

1. Dalbeth N, et al. Gout. *Lancet*. 2021;397:1843-1855.
2. Leask MP, et al. The pathogenesis of gout: molecular insights from genetic, epigenomic and transcriptomic studies. *Nature Reviews Rheumatology*. 2024;20:510-523.
3. FitzGerald JD, et al. 2020 American College of Rheumatology Guideline for the Management of Gout. *Arthritis Care & Research*. 2020;72:744-760.
4. Deconstruction of tophi and synovium defines SPP1+ macrophages involved in extracellular matrix remodelling in gout. *Annals of the Rheumatic Diseases*. 2025. PMID: 41107120. DOI: [10.1016/j.ard.2025.09.003](https://doi.org/10.1016/j.ard.2025.09.003).

## 1. Central Question: Gout Is More Than Hyperuricaemia

The conventional explanation of gout begins with hyperuricaemia. When serum urate exceeds its solubility threshold, monosodium urate crystals, or MSU crystals, can deposit in local joint tissues and trigger acute inflammation. This framework explains acute gout flares well, but it is less sufficient for explaining chronic tophus formation, local joint destruction, fibrosis, and bone erosion.

The central question has therefore shifted from why urate levels rise to why specific joints develop persistent pathological microenvironments. In this broader view, gout is both a systemic metabolic disease and a local tissue-remodeling disease.

## 2. The Classical Model: MSU Crystals Drive Acute Inflammation

During an acute gout flare, MSU crystals are the key inflammatory trigger. After macrophages phagocytose MSU crystals, the NLRP3 inflammasome is activated. This promotes caspase-1 activation, IL-1 beta and IL-18 release, and pyroptotic cell death.

The acute inflammatory cascade can be summarized as:

```text
MSU crystals
    |
macrophage phagocytosis
    |
NLRP3 inflammasome activation
    |
caspase-1 activation
    |
IL-1 beta release and pyroptosis
    |
acute gout flare
```

This model emphasizes the direct interaction between crystals and innate immunity. It explains the rapid onset of acute inflammation and provides the rationale for therapies targeting IL-1 beta-related inflammatory pathways.

## 3. From Systemic Metabolism to Local Tissue Context

The upstream basis of gout is disrupted urate homeostasis. Urate transporter genes such as **SLC2A9**, **SLC22A12**, and **ABCG2** regulate urate reabsorption and excretion, thereby influencing the risk of hyperuricaemia. GWAS and related genetic studies provide a systemic explanation for urate burden.

However, hyperuricaemia alone does not explain why only certain joints develop severe inflammation, recurrent flares, or chronic tophi. Recent studies increasingly suggest that the local joint microenvironment influences MSU crystal deposition, persistence, and progression toward chronic tissue damage.

This conceptual transition can be organized into four levels:

1. Cartilage and extracellular matrix components may influence MSU crystallization and inflammatory cell recruitment.
2. Damaged joints may form permissive local niches that explain anatomical preference and recurrence.
3. SRS imaging and synovial organoid models can visualize the spatiotemporal process of MSU crystal deposition.
4. Single-cell and spatial transcriptomics can deconstruct the immune, stromal, and bone-related architecture of established tophi.

The logic of gout research is therefore expanding from metabolic disturbance and crystal deposition toward crystal-induced local tissue ecology.

## 4. Single-Cell and Spatial Omics: The Gouty Tophus as an Organized Lesion

A gouty tophus is not merely a passive aggregate of urate crystals. It is a chronic pathological structure composed of MSU crystals, immune cells, fibroblasts, vascular components, bone-lineage cells, and extracellular matrix.

Single-cell transcriptomics and spatial transcriptomics are valuable because they separate this complex lesion into cell states, signaling programs, and spatial domains. The central analytical task is not only to ask which cell types are present, but also to ask where they are located, how they interact, and which signaling axes maintain the lesion.

## 5. SPP1+ TGAMs: A Macrophage State Linking Inflammation and Remodeling

One of the key findings is the identification of **SPP1+ tophus-associated macrophages**, referred to as SPP1+ TGAMs. Here, the term refers to macrophages enriched in gouty tophus lesions.

SPP1+ TGAMs express genes such as **SPP1**, **MMP9**, and **CHI3L1**. This profile suggests that they are not simply acute inflammatory macrophages. Instead, they resemble a chronic inflammatory and tissue-remodeling macrophage state. MMP9 points toward matrix degradation and remodeling; CHI3L1 is associated with inflammation, fibrosis, and tissue repair; SPP1 may mediate adhesion, migration, and communication between immune and stromal cells.

The significance of SPP1+ TGAMs is that they may connect MSU-induced inflammation with extracellular matrix remodeling, fibrosis, osteoclast differentiation, and structural joint damage.

## 6. Cell-Cell Communication: The SPP1-CD44 Axis

Compared with intercritical gout, gouty tophus lesions show markedly enhanced cell-cell communication. The **SPP1-CD44** interaction emerges as a prominent ligand-receptor axis linking SPP1+ TGAMs with fibroblasts, osteoblast-lineage cells, osteoclast-lineage cells, and regulatory T cells.

This observation is important because it reframes macrophages as organizers of the local pathological niche rather than merely executors of inflammation. Through SPP1-CD44 signaling, macrophages may influence fibroblast activation, collagen deposition, bone remodeling, and immune regulation. This could help explain how a crystal deposition site evolves into a stable chronic tissue lesion.

## 7. Spatial Zonation: Immune-Stromal Interaction and Structural Remodeling

Spatial analysis further suggests that the gouty tophus contains regionally organized signaling programs. SPP1 signaling is enriched in the corona zone, whereas collagen signaling is more prominent in the fibrovascular zone.

This can be conceptualized as two connected spatial layers:

```text
corona zone
    immune-stromal interaction
    SPP1-CD44 signaling
    macrophage-fibroblast and macrophage-bone-lineage crosstalk

fibrovascular zone
    collagen signaling
    extracellular matrix organization
    fibrosis and structural remodeling
```

This spatial pattern indicates that the gouty tophus is not a homogeneous inflammatory mass. It is a compartmentalized pathological niche: the inner region is more associated with SPP1-driven immune-stromal communication, whereas the outer region is more associated with collagen-driven structural remodeling.

## 8. Integrated Disease Model

The overall disease logic can be summarized as:

```text
persistent hyperuricaemia
    |
MSU crystal deposition in joints
    |
local tophus microenvironment formation
    |
expansion of SPP1+ TGAMs
    |
SPP1-CD44 signaling activation
    |
crosstalk with fibroblasts, osteoblast-lineage cells,
osteoclast-lineage cells, and regulatory T cells
    |
ECM remodeling, fibrosis, and osteoclast differentiation
    |
tophus maturation and joint damage
```

This model integrates systemic urate dysregulation, local crystal deposition, macrophage state transition, intercellular communication, and spatial tissue remodeling into a single pathological sequence.

## 9. Interpretation

The value of this framework is not limited to the discovery of a marker-defined macrophage cluster. More importantly, it redefines the gouty tophus as a chronic spatial microenvironment constructed by immune cells, stromal cells, bone-lineage cells, and extracellular matrix.

Compared with the linear **MSU-NLRP3-IL-1 beta** model of acute gout, chronic gouty tophus formation is better understood as a tissue-ecology process. From a single-cell perspective, SPP1+ TGAMs provide a disease-associated macrophage state. From a spatial perspective, the separation between the corona zone and fibrovascular zone explains how the lesion acquires structural stability. From a mechanistic perspective, the SPP1-CD44 axis may connect chronic inflammation with extracellular matrix remodeling.

## 10. Open Questions

1. Are SPP1+ TGAMs drivers of tophus formation, or are they consequences of a mature tophus microenvironment?
2. Does the SPP1-CD44 axis represent a therapeutically actionable pathway?
3. Is the SPP1+ TGAM-associated niche reversible after effective urate-lowering therapy?
4. Does a similar macrophage-stromal remodeling axis exist in other crystal-associated or chronic inflammatory joint diseases?
5. How can GWAS-defined systemic urate-regulatory genes be connected to local cell-state transitions in joint tissues?

## Summary

The main conceptual trajectory is that gout research is moving from systemic urate metabolism and acute inflammatory cascades toward local tissue microenvironments and spatial disease niches. MSU crystals initiate acute inflammation, but chronic tophus formation requires a broader framework that includes SPP1+ TGAMs, SPP1-CD44 communication, extracellular matrix remodeling, and spatially organized tissue structure.

In this view, gouty tophus formation should not be understood simply as the endpoint of urate crystal deposition. It is a chronic tissue-remodeling process jointly shaped by crystals, immune cells, stromal cells, bone-lineage cells, and extracellular matrix.
