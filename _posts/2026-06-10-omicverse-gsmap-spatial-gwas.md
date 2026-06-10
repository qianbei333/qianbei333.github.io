---
layout: post
title: "Spatially Resolved GWAS Mapping with OmicVerse gsMap"
date: 2026-06-10 12:00:00 +0800
categories: gwas spatial-transcriptomics omicverse gsmap
---

Today I studied the OmicVerse genetics tutorial **GWAS pipeline 3 — Spatially Resolved GWAS Mapping**, which demonstrates how to use the gsMap workflow to connect GWAS summary statistics with spatial transcriptomic tissue architecture.

Official tutorial: [Spatially Resolved GWAS Mapping](https://omicverse.readthedocs.io/en/latest/Tutorials-genetics/t_genetics_03_spatially_resolved_gwas.html)

Code used in my implementation:

- [run_gsmap_spatial_gwas.py](/assets/code/gsmap-spatial-gwas/run_gsmap_spatial_gwas.py)
- [gsmap_spatial_gwas.sh](/assets/code/gsmap-spatial-gwas/gsmap_spatial_gwas.sh)

## Background

GWAS identifies genomic loci associated with complex traits, but its output is usually not directly spatial or cell-type resolved. For many biological questions, especially in developmental biology, neurobiology, immunology, and tissue pathology, the next question is not only which loci are associated with a trait, but where in tissue those genetic signals may become biologically relevant.

The OmicVerse gsMap workflow addresses this gap by integrating spatial transcriptomic data with GWAS summary statistics. Conceptually, it asks whether genetic signals from a trait are enriched in spatially defined molecular programs, and then maps those signals back to tissue coordinates.

This makes gsMap useful for moving from trait-associated genetic signals toward spatially interpretable biological hypotheses.

## Tutorial Logic

The official OmicVerse tutorial presents a complete gsMap example using the provided spatial transcriptomic dataset and GWAS summary statistics. The core workflow is:

```text
spatial transcriptomics data
    |
find_latent_representation
    |
latent_to_gene
    |
generate_ldscore
    |
spatial_ldsc
    |
cauchy_combination
    |
spatial visualisation and gene-level diagnostics
```

Each step plays a distinct role.

`find_latent_representation` learns a latent representation from the spatial transcriptomic dataset. This step compresses spatial gene expression patterns into a lower-dimensional representation that can later be connected to gene-level signals.

`latent_to_gene` maps the latent representation back to gene-level scores. In the mouse example, this also requires mouse-human homolog mapping so that spatial transcriptomic genes can be connected to human GWAS summary statistics.

`generate_ldscore` prepares LD score files for the spatially resolved analysis.

`spatial_ldsc` performs spatial LDSC using GWAS summary statistics and the gsMap resource directory.

`cauchy_combination` aggregates spot-level signals into annotation-level significance, providing a way to summarise spatial GWAS enrichment across annotated tissue domains.

The final plotting steps visualise spatial gsMap p-values, Cauchy-combination results, gene expression, gene specificity scores, and top diagnostic genes.

## My Implementation

I rewrote the tutorial into two executable scripts: a Python pipeline and an HPC submission wrapper.

The Python script, `run_gsmap_spatial_gwas.py`, is the main analysis workflow. It reads the spatial transcriptomic `.h5ad` file, creates an OmicVerse gsMap object, runs latent representation learning, converts latent features to gene scores, generates LD scores, performs spatial LDSC, combines p-values with the Cauchy method, and saves several diagnostic figures.

The shell script, `gsmap_spatial_gwas.sh`, is designed for a cluster environment. It defines SGE job parameters, starts a Singularity container, activates the `omicverse` conda environment, exports thread and plotting variables, and runs the Python workflow inside the container.

This separation is useful because the Python script describes the biological and computational workflow, while the shell script records the execution environment needed to reproduce the analysis on an HPC system.

## Engineering Details

The Python script uses environment variables to make the pipeline portable:

```text
GSMAP_BASE_DIR
GSMAP_DATASET
GSMAP_SUMSTATS
GSMAP_RESOURCE_DIR
GSMAP_OUTPUT_DIR
GSMAP_SAMPLE_NAME
GSMAP_TRAIT_NAME
GSMAP_ANNOTATION
GSMAP_DATA_LAYER
```

This design avoids hard-coding every path. The same script can be reused with another spatial dataset, another GWAS summary statistics file, or another trait simply by changing environment variables.

The script also controls computational resources:

```text
GSMAP_NUM_PROCESSES
GSMAP_THREADS
GSMAP_EPOCHS
GSMAP_SPOTS_PER_CHUNK
```

This is important because gsMap can be computationally heavy. Thread control prevents BLAS, MKL, NumExpr, and Numba from overusing CPU resources inside a scheduled cluster job.

The workflow is also configured for non-interactive execution. Matplotlib uses the `Agg` backend, warnings are suppressed where appropriate, and all figures are saved to an output directory instead of displayed interactively.

## Output

The pipeline saves figures under:

```text
GSMAP_OUTPUT_DIR/figures
```

The current plotting outputs include:

1. Spatial map of gsMap log p-values for the selected trait.
2. Cauchy-combination bar plot across annotations.
3. Expression versus gene specificity score for an example gene, defaulting to `MAP2`.
4. Spatial gene specificity score maps for the top diagnostic genes, if the diagnostic CSV is available.

These outputs are useful because they show the analysis at three levels: spatial trait signal, annotation-level enrichment, and gene-level contribution.

## Why This Matters

The biological value of spatially resolved GWAS mapping is that it can connect statistical genetics with tissue organisation. A GWAS locus alone often remains abstract. Spatial transcriptomics adds context by asking whether trait-associated signals converge on particular tissue regions, cellular programs, or anatomical domains.

For my own research interests, this type of method is especially attractive because it offers a bridge between:

```text
GWAS
    |
single-cell or spatial transcriptomics
    |
cell-state and tissue-domain interpretation
    |
mechanistic hypothesis generation
```

This is also conceptually related to my recent thinking about using GWAS, scPagwas, gsMap, and single-cell multiome data to strengthen mechanistic models. GWAS can identify inherited risk signals, single-cell methods can map these signals to disease-associated cell states, and spatial methods can localise them to tissue microenvironments.

## Practical Notes

Several points are worth remembering for future runs.

First, the homolog file is essential when using mouse spatial data with human GWAS summary statistics. The script explicitly checks for `mouse_human_homologs.txt` before running `latent_to_gene`.

Second, path management matters. The Singularity wrapper binds the host working directory to `/work`, so all paths inside the container should be interpreted from the container perspective.

Third, quick-mode parameters such as `spots_per_chunk_quick_mode` are useful for making the analysis more manageable on large spatial datasets.

Fourth, diagnostic plots should not be treated as decorative outputs. They are important sanity checks for whether the spatial GWAS signal, annotation-level enrichment, and gene-level specificity are biologically coherent.

## Take-Home Message

This tutorial helped me understand how gsMap turns spatial transcriptomic data and GWAS summary statistics into spatially interpretable genetic enrichment maps. My scripts convert the notebook-style workflow into a reproducible HPC-oriented pipeline, making it easier to rerun the analysis with different traits, datasets, and resource configurations.

The broader lesson is that spatial omics can make GWAS more anatomically interpretable. Instead of stopping at trait-associated loci, we can begin to ask where in tissue genetic risk may act, which molecular programs carry the signal, and which cell states or spatial domains deserve deeper mechanistic follow-up.
