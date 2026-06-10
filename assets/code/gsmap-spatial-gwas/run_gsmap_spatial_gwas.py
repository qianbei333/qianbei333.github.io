#!/usr/bin/env python

import os
import sys
import warnings
from pathlib import Path

os.environ.setdefault("MPLBACKEND", "Agg")

for key in [
    "OMP_NUM_THREADS",
    "OPENBLAS_NUM_THREADS",
    "MKL_NUM_THREADS",
    "MKL_DOMAIN_NUM_THREADS",
    "NUMEXPR_NUM_THREADS",
    "NUMBA_NUM_THREADS",
]:
    os.environ.setdefault(key, os.environ.get("GSMAP_THREADS", "1"))

warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import omicverse as ov
import pandas as pd
import scanpy as sc


def env_int(name, default):
    return int(os.environ.get(name, default))


def dense_vector(x):
    if hasattr(x, "toarray"):
        return x.toarray().ravel()
    return np.asarray(x).ravel()


def main():
    try:
        sys.stdout.reconfigure(line_buffering=True)
    except Exception:
        pass

    np.random.seed(0)
    ov.plot_set()

    base_dir = Path(os.environ.get("GSMAP_BASE_DIR", "/work/gsMap"))
    dataset_path = Path(os.environ.get(
        "GSMAP_DATASET",
        base_dir / "gsMap_example_data/ST/E16.5_E1S1.MOSTA.h5ad",
    ))
    sumstats_file = Path(os.environ.get(
        "GSMAP_SUMSTATS",
        base_dir / "gsMap_example_data/GWAS/IQ_NG_2018.sumstats.gz",
    ))
    resource_dir = Path(os.environ.get("GSMAP_RESOURCE_DIR", base_dir / "gsMap_resource"))
    output_dir = Path(os.environ.get("GSMAP_OUTPUT_DIR", base_dir / "gsmap_tutorial_output"))
    fig_dir = output_dir / "figures"
    fig_dir.mkdir(parents=True, exist_ok=True)

    sample_name = os.environ.get("GSMAP_SAMPLE_NAME", "e16_5_e1s1_mosta_full")
    trait_name = os.environ.get("GSMAP_TRAIT_NAME", "IQ")
    annotation = os.environ.get("GSMAP_ANNOTATION", "annotation")
    data_layer = os.environ.get("GSMAP_DATA_LAYER", "count")

    epochs = env_int("GSMAP_EPOCHS", 300)
    num_processes = env_int("GSMAP_NUM_PROCESSES", 6)
    spots_per_chunk = env_int("GSMAP_SPOTS_PER_CHUNK", 1000)

    print("[INFO] Python    :", sys.executable)
    print("[INFO] OmicVerse :", getattr(ov, "__version__", "unknown"))
    print("[INFO] Data      :", dataset_path)
    print("[INFO] Sumstats  :", sumstats_file)
    print("[INFO] Resource  :", resource_dir)
    print("[INFO] Output    :", output_dir)

    for path in [dataset_path, sumstats_file, resource_dir]:
        if not path.exists():
            raise FileNotFoundError(path)

    homolog_file = resource_dir / "homologs/mouse_human_homologs.txt"
    if not homolog_file.exists():
        raise FileNotFoundError(homolog_file)

    print("[1/8] Read h5ad")
    adata = sc.read_h5ad(dataset_path)
    adata.obs[annotation] = adata.obs[annotation].astype("category")
    print(adata)

    print("[2/8] Create gsMap object")
    gsmap_object = ov.genetics.gsmap(
        adata,
        workdir=str(output_dir),
        sample_name=sample_name,
        annotation=annotation,
    )

    print("[3/8] Find latent representation")
    latent_path = gsmap_object.find_latent_representation(
        data_layer=data_layer,
        epochs=epochs,
        feat_cell=3000,
        feat_hidden1=256,
        feat_hidden2=128,
        gat_hidden1=64,
        gat_hidden2=30,
        n_comps=300,
        n_neighbors=11,
        nheads=3,
    )
    print("[INFO] latent_path:", latent_path)

    print("[4/8] Latent to gene")
    marker_path = gsmap_object.latent_to_gene(
        input_hdf5_path=str(latent_path),
        latent_representation="latent_GVAE",
        num_neighbour=51,
        num_neighbour_spatial=201,
        species="MOUSE_GENE_SYM",
        homolog_file=str(homolog_file),
    )
    print("[INFO] marker_path:", marker_path)

    print("[5/8] Generate LD score")
    ldscore_dir = gsmap_object.generate_ldscore(gsmap_resource_dir=str(resource_dir))
    print("[INFO] ldscore_dir:", ldscore_dir)

    print("[6/8] Spatial LDSC")
    ldsc_dir = gsmap_object.spatial_ldsc(
        gsmap_resource_dir=str(resource_dir),
        sumstats_file=str(sumstats_file),
        trait_name=trait_name,
        num_processes=num_processes,
        n_blocks=200,
        spots_per_chunk_quick_mode=spots_per_chunk,
    )
    print("[INFO] ldsc_dir:", ldsc_dir)

    print("[7/8] Cauchy combination")
    cauchy_file = gsmap_object.cauchy_combination(
        trait_name=trait_name,
        annotation=annotation,
    )
    print("[INFO] cauchy_file:", cauchy_file)

    print("[8/8] Save plots")
    adata_plot = gsmap_object._get_latent_adata()

    fig, ax = plt.subplots(figsize=(3, 4))
    ov.pl.embedding(
        adata_plot,
        basis="spatial",
        color=[f"{trait_name}_gsmap_logp"],
        cmap="YlOrRd",
        size=1.25,
        ax=ax,
        show=False,
    )
    fig.tight_layout()
    fig.savefig(fig_dir / f"{trait_name}_gsmap_logp_spatial.png", dpi=300)
    plt.close(fig)

    gsmap_object.plot_cauchy_bar(trait_name, cmap="Blues", figsize=(6, 8))
    plt.tight_layout()
    plt.savefig(fig_dir / f"{trait_name}_cauchy_bar.png", dpi=300)
    plt.close("all")

    adata_plot = ov.read(gsmap_object.hdf5_with_latent_path)
    mk_score = pd.read_feather(gsmap_object.mkscore_feather_path).set_index("HUMAN_GENE_SYM").T

    gene = os.environ.get("GSMAP_EXAMPLE_GENE", "MAP2")
    if gene in adata_plot.var_names and gene in mk_score.columns:
        adata_plot.obs[f"{gene}_expr"] = dense_vector(adata_plot[:, gene].X)
        adata_plot.obs[f"{gene}_gss"] = mk_score[gene].reindex(adata_plot.obs_names).values

        fig, axes = plt.subplots(1, 2, figsize=(6, 4))
        ov.pl.embedding(adata_plot, basis="spatial", color=f"{gene}_expr",
                        cmap="YlOrRd", size=1.25, title=f"{gene} Expression",
                        ax=axes[0], show=False)
        ov.pl.embedding(adata_plot, basis="spatial", color=f"{gene}_gss",
                        cmap="YlOrRd", size=1.25, title=f"{gene} GSS",
                        ax=axes[1], show=False)
        fig.tight_layout()
        fig.savefig(fig_dir / f"{gene}_expression_vs_gss.png", dpi=300)
        plt.close(fig)

    gene_diag_path = (
        Path(gsmap_object.workdir)
        / gsmap_object.sample_name
        / "report"
        / trait_name
        / f"{gsmap_object.sample_name}_{trait_name}_Gene_Diagnostic_Info.csv"
    )
    if gene_diag_path.exists():
        gene_info = pd.read_csv(gene_diag_path)
        top_genes = gene_info.Gene.iloc[:5].tolist()
        print("[INFO] Top 5 genes:", top_genes)

        fig, axes = plt.subplots(2, 3, figsize=(9, 8))
        axes = axes.flatten()
        plotted = 0
        for gene_name in top_genes:
            if gene_name not in mk_score.columns:
                continue
            adata_plot.obs[f"{gene_name}_gss"] = mk_score[gene_name].reindex(adata_plot.obs_names).values
            ov.pl.embedding(
                adata_plot,
                basis="spatial",
                color=f"{gene_name}_gss",
                cmap="YlOrRd",
                size=1.25,
                ax=axes[plotted],
                show=False,
            )
            axes[plotted].set_title(f"{gene_name} GSS", fontsize=9)
            plotted += 1

        for idx in range(plotted, len(axes)):
            axes[idx].set_visible(False)

        fig.tight_layout()
        fig.savefig(fig_dir / "top5_gene_gss.png", dpi=300)
        plt.close(fig)

    print("[DONE] Figures:", fig_dir)
    print("[DONE] Output :", output_dir)


if __name__ == "__main__":
    main()
