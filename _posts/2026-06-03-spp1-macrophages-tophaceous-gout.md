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

This reading note is based primarily on the full text of the following article:

Xu H, Liu Z, Zhou X, Ji X, Liu X, Zhu X, Lu L, Dalbeth N, He R, Hua Y. **Deconstruction of tophi and synovium defines SPP1+ macrophages involved in extracellular matrix remodelling in gout.** *Annals of the Rheumatic Diseases*. 2025;84:2088-2102. DOI: [10.1016/j.ard.2025.09.003](https://doi.org/10.1016/j.ard.2025.09.003).

## Background and Rationale

Gout is driven by elevated serum urate and the deposition of monosodium urate crystals in joints. The mechanisms of acute gout flares are relatively well established: MSU crystals activate innate immune responses, particularly the NLRP3 inflammasome and IL-1 beta signalling. However, the biology of tophaceous gout remains less clearly defined.

The central gap addressed by this paper is not the initiation of an acute flare, but the formation of tophi as chronic, organised lesions. Previous histological work has shown that tophi contain a central MSU crystal core, a macrophage-rich corona zone, and an outer fibrovascular zone. This layered architecture implies that tophus formation is not only a crystal deposition event, but also a spatially organised immune-stromal remodeling process.

The authors therefore ask how immune cells, stromal cells, and bone-related cells are organised within tophi and how their interactions may contribute to extracellular matrix remodelling, fibrosis, osteoclast differentiation, and joint destruction.

## Study Design

The study integrates single-cell RNA sequencing and spatial transcriptomics to compare synovial tissue from patients with intercritical gout without tophi and tissue from patients with tophaceous gout. After quality control, the authors analysed 44,221 cells from synovial or tophus samples.

The main experimental and analytical components include:

1. Single-cell RNA sequencing to define immune, stromal, and bone-related cell populations across disease stages.
2. Spatial transcriptomics to map gene expression patterns in the corona and fibrovascular zones of tophi.
3. RCTD-based cell-type decomposition to infer the cellular composition of spatial transcriptomic spots.
4. Pseudotime and spatial trajectory analyses to infer macrophage-to-osteoclast progression.
5. Differential gene expression and pathway enrichment analyses to identify stage-specific transcriptional programs.
6. Flow cytometry and immunofluorescence to validate macrophage marker coexpression and spatial localisation.
7. Cell-cell communication analysis to identify ligand-receptor interactions between macrophages, fibroblasts, osteoblasts, osteoclasts, and T cells.
8. Differential causal inference and Mendelian randomisation to explore regulatory networks and possible causal relationships.

This design is important because the authors do not rely on single-cell data alone. They combine cell-state discovery with spatial localisation and experimental validation, which makes the proposed mechanism more tissue-context aware.

## Result 1: Tophi Contain Spatially Distinct Cellular Niches

The spatial transcriptomic analysis maps cell populations across the corona and fibrovascular zones of tophi. The authors analysed 4313 spatial spots and identified distinct spot clusters across these two anatomical regions. By integrating the spatial data with single-cell profiles, they inferred the cellular composition of each spot.

A key finding is that the corona and fibrovascular zones are not simply different histological layers; they also differ in cellular composition and inferred biological activity. Fibroblasts, mast cells, and proliferating cells were enriched in the corona zone, whereas osteoblast-related populations were more prominent in the fibrovascular zone. Spatial trajectory analysis further suggested macrophage-to-osteoclast progression, with transition markers enriched in pathways related to lysosomal activity, consistent with osteoclast differentiation.

This result establishes the spatial foundation of the paper: tophi are compartmentalised lesions in which immune and stromal programs are regionally organised.

## Result 2: SPP1+ TGAMs Are a Tophus-Specific Macrophage Population

The authors next focused on macrophages because macrophages are central to both acute gout inflammation and the cellular structure of tophi. Unsupervised clustering identified multiple macrophage subclusters. Among them, M0, M6, and M9 were enriched in tophaceous gout and were classified as tophaceous gout-associated macrophages, or TGAMs. In contrast, M1, M3, and M5 were enriched in intercritical gout and were classified as intercritical gout-associated macrophages.

Pseudotime analysis placed intercritical gout-associated macrophages near the beginning of the trajectory and TGAMs near the endpoint, suggesting a disease-stage-associated macrophage transition. The key molecular distinction was the reciprocal pattern between **SPP1** and **FOLR2**. TGAMs were enriched for **SPP1**, whereas intercritical macrophages were enriched for **FOLR2**.

The TGAM population showed high expression of **SPP1**, **MMP9**, and **CHI3L1**. These markers point to a macrophage state associated with extracellular matrix regulation, tissue remodeling, and chronic inflammation. Flow cytometry further supported the increased presence of SPP1/CHI3L1, SPP1/MMP9, and CHI3L1/MMP9 double-positive macrophage populations in tophaceous gout.

The main interpretation is that SPP1+ TGAMs are not merely inflammatory macrophages. They represent a tophus-associated macrophage state with matrix-remodeling and osteoclast-related potential.

## Result 3: TGAMs Differ From Acute Flare-Associated Macrophages

To distinguish chronic tophus biology from acute flare biology, the authors compared TGAMs with macrophages from gout flare-associated synovial fluid. This comparison is conceptually important because acute gout flares and tophaceous gout are often discussed under the same disease umbrella, but the cellular programs are not identical.

TGAMs showed upregulation of genes related to extracellular matrix remodeling, including matrix metalloproteinases and collagen-related genes such as **COL6A2** and **COL6A3**. Pathway enrichment highlighted protein digestion and absorption, ECM-receptor interaction, and related remodeling pathways.

This indicates that TGAMs are more closely aligned with chronic tissue remodeling than with the purely acute inflammatory macrophage state. The authors also used Mendelian randomisation to support a relationship between SPP1 expression and gout-related risk, suggesting that SPP1 may not be only a marker but may also be mechanistically relevant.

## Result 4: Fibroblasts and Osteoblasts Shift From Inflammatory to ECM-Regulatory Programs

The paper then expands the analysis from macrophages to stromal and bone-related cells. Fibroblasts and osteoblasts exhibited disease-stage-specific transcriptional states. In intercritical gout, fibroblast and osteoblast subsets were more associated with inflammatory pathways. In tophaceous gout, they shifted toward extracellular matrix regulation, protein remodeling, focal adhesion, and ECM-receptor interaction pathways.

The authors identified tophaceous gout-associated fibroblast states, including TGAF-1 and TGAF-2. TGAF-2 was particularly interesting because it shared transcriptional features with SPP1+ TGAMs, including expression of **SPP1**, **MMP9**, and **CD68**. CytoTRACE and pseudotime analyses suggested a close relationship between TGAMs and TGAF-2, raising the possibility of macrophage-fibroblast intermediate states.

Immunofluorescence staining further supported this idea. Cells coexpressing S100A4, SPP1, and CD68 were enriched in the corona zone, providing spatial and protein-level evidence for a macrophage-fibroblast-associated phenotype in tophi.

The biological implication is that the tophus microenvironment may promote cellular plasticity or convergence between macrophage and fibroblast-like programs, thereby linking chronic inflammation to fibrosis and matrix remodeling.

## Result 5: SPP1-CD44 Signalling Is Activated in the Corona Zone

Cell-cell communication analysis showed stronger and more frequent interactions in tophaceous gout than in intercritical gout. Among the inferred ligand-receptor interactions, the **SPP1-CD44** axis was prominent between TGAMs and fibroblasts or osteoblasts.

Spatial communication analysis added an important layer. In the corona zone, SPP1-related signalling was dominant, whereas in the fibrovascular zone, complement and collagen-related pathways were more prominent. In the SPP1 pathway, macrophages, fibroblasts, and osteoblasts could act as senders or receivers, suggesting a local communication network rather than a one-directional signal.

The genes regulated downstream of SPP1 signalling were enriched for focal adhesion, ECM-receptor interaction, and protein digestion pathways. This supports the authors' argument that SPP1-CD44 signalling may connect macrophage activation to stromal remodeling and bone-related tissue damage.

## Result 6: T-Cell States Also Change During Tophus Development

The authors also analysed T-cell populations. CD4+ naive T cells were more abundant in intercritical gout, whereas regulatory T cells marked by **CTLA4** and **FOXP3** were increased in tophaceous gout. Pseudotime analysis suggested a trajectory from naive CD4+ T cells toward regulatory T-cell states.

Cell communication analysis further showed stronger interactions between TGAMs and regulatory T cells than between intercritical macrophages and regulatory T cells. Receptor-ligand pairs such as **PPIA-BSG** and **SPP1-CD44** were highlighted.

This result suggests that tophus development is not only a macrophage-stromal process. It may also involve immune-regulatory remodeling, in which Tregs participate in the local chronic inflammatory niche.

## Discussion and Mechanistic Interpretation

The major contribution of this paper is the identification of SPP1+ TGAMs as a macrophage population linking chronic inflammation, extracellular matrix remodeling, fibrosis, osteoclast differentiation, and tophus-associated joint damage.

The authors' model can be interpreted as follows:

```text
intercritical gout
    |
macrophage and stromal inflammatory programs
    |
tophus formation
    |
SPP1+ / MMP9+ / CHI3L1+ TGAM expansion
    |
SPP1-CD44 and integrin-mediated immune-stromal communication
    |
fibroblast and osteoblast ECM-regulatory programs
    |
fibrosis, osteoclast differentiation, bone erosion, and joint damage
```

A key strength of the study is that it connects cell-state discovery with spatial architecture. The corona zone appears to be an active immune-stromal communication region enriched for SPP1 signalling, while the fibrovascular zone is more closely associated with collagen signalling and structural remodeling. This spatial division helps explain why the tophus behaves as an organised granuloma-like lesion rather than a simple crystal deposit.

Another important point is that SPP1+ TGAMs may have dual functions. They retain inflammatory features, but they also acquire matrix-remodeling and fibroblast-like properties. This dual phenotype makes them a plausible cellular bridge between chronic inflammation and structural tissue damage.

## Limitations

The authors also acknowledge several limitations. First, the spatial resolution of the 10x Visium platform is limited, so each spot may contain multiple cells. This restricts the precision of cell-cell interaction inference and the identification of rare transitional cell states. Second, the number and diversity of tissue samples are limited, which is understandable given the difficulty of obtaining human tophus and synovial tissues but still affects generalisability. Third, computational trajectory and communication analyses require further experimental validation. Lineage tracing, co-culture experiments, and perturbation assays would be valuable for testing whether TGAMs directly drive fibroblast activation, osteoclast differentiation, or matrix remodeling.

## My Extension: How to Further Strengthen the Mechanistic Model

To further strengthen the evidence supporting this article's mechanistic model, future work could add evidence from three complementary levels.

First, at the genetic level, GWAS could be used to identify genetic risk signals associated with gout, tophus formation, or severe joint damage. This would help connect the local cellular findings with inherited disease susceptibility.

Second, at the cellular level, methods such as **scPagwas** could map GWAS signals onto single-cell subpopulations. This would help determine whether genetic risk is preferentially carried by SPP1+ TGAMs, TGAFs, Tregs, osteoblast-lineage cells, or other disease-associated cell states. Such analysis would move the interpretation from marker-based cell annotation toward genetically informed prioritisation of pathogenic cell types.

Third, at the spatial level, tools such as **gsMap** could be used to project genetic risk signals into spatial domains of the tophus. This would help determine whether risk signals are enriched in the corona zone, the fibrovascular zone, or other local microenvironments. If SPP1+ TGAM-associated genetic signals localise to the corona zone while collagen-remodeling signals localise to the fibrovascular zone, the spatial model proposed by the authors would become more compelling.

In addition, scATAC-seq or single-cell multiome profiling could add a regulatory layer. These approaches could identify the chromatin accessibility programs, transcription factors, and enhancer landscapes that drive SPP1+ TGAM formation. This would help explain why macrophages in the tophus acquire this specific SPP1+ / MMP9+ / CHI3L1+ state, rather than only describing the state after it has already formed.

Together, genetic mapping, single-cell genetic prioritisation, spatial localisation, and epigenomic regulation could support the authors' model from genetic, cellular, spatial, and regulatory perspectives.

## Take-Home Message

This paper reframes tophaceous gout as a spatially organised immune-stromal remodeling disease. The key finding is that SPP1+ TGAMs are enriched in tophi and may coordinate macrophage-fibroblast-osteoblast communication through SPP1-CD44 and related ECM-remodeling pathways. By integrating single-cell transcriptomics, spatial transcriptomics, validation experiments, and causal inference, the study provides a mechanistic framework linking chronic inflammation to fibrosis, osteoclast differentiation, tophus maturation, and joint damage in gout.
