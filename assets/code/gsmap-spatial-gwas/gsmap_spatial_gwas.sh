#!/usr/bin/env bash
#$ -cwd
#$ -j y
#$ -o logs/gsmap_spatial_gwas_$JOB_ID.log
#$ -l vf=80G
#$ -l num_proc=6
#$ -P P23Z10200N0866
#$ -N gsmap_gwas

set -euo pipefail

HOST_WORK_DIR="${HOST_WORK_DIR:-/dellfsqd1/ST_OCEAN/C_OCEAN/USERS/c-liuzhi}"
SIF_IMAGE="${SIF_IMAGE:-${HOST_WORK_DIR}/ubuntu_20.04.sif}"
CONDA_ROOT="${CONDA_ROOT:-/work/miniconda_container}"
CONDA_ENV="${CONDA_ENV:-omicverse}"
PROJECT_DIR="${PROJECT_DIR:-/work/gsMap}"
PY_SCRIPT="${PY_SCRIPT:-${PROJECT_DIR}/run_gsmap_spatial_gwas.py}"

GSMAP_NUM_PROCESSES="${GSMAP_NUM_PROCESSES:-6}"
GSMAP_THREADS="${GSMAP_THREADS:-1}"
GSMAP_EPOCHS="${GSMAP_EPOCHS:-300}"
GSMAP_SPOTS_PER_CHUNK="${GSMAP_SPOTS_PER_CHUNK:-1000}"

mkdir -p logs

echo "============================================================"
echo "[INFO] Time       : $(date '+%Y-%m-%d %H:%M:%S')"
echo "[INFO] Host       : $(hostname)"
echo "[INFO] Job ID     : ${JOB_ID:-manual}"
echo "[INFO] Work Dir   : $(pwd)"
echo "[INFO] Image      : ${SIF_IMAGE}"
echo "[INFO] Project    : ${PROJECT_DIR}"
echo "[INFO] Python     : ${PY_SCRIPT}"
echo "[INFO] Cores      : ${GSMAP_NUM_PROCESSES}"
echo "[INFO] Threads    : ${GSMAP_THREADS}"
echo "============================================================"

singularity exec --cleanenv \
  --pwd /work \
  -B "${HOST_WORK_DIR}:/work" \
  -B /zfsqd2:/zfsqd2 \
  "${SIF_IMAGE}" \
  /bin/bash -s <<EOF
set -euo pipefail

export HOME=/work
export XDG_CACHE_HOME=/work/.cache
export CONDA_PKGS_DIRS=/work/.conda/pkgs
export CONDA_ENVS_PATH=/work/.conda/envs
export CONDARC=/work/.condarc
export TMPDIR=/tmp

mkdir -p /work/.cache /work/.conda/pkgs /work/.conda/envs

source "${CONDA_ROOT}/bin/activate"
conda activate "${CONDA_ENV}"

export LD_LIBRARY_PATH="\${CONDA_PREFIX}/lib:\${LD_LIBRARY_PATH:-}"
export PATH="\${CONDA_PREFIX}/bin:\${PATH}"

export GSMAP_NUM_PROCESSES="${GSMAP_NUM_PROCESSES}"
export GSMAP_THREADS="${GSMAP_THREADS}"
export GSMAP_EPOCHS="${GSMAP_EPOCHS}"
export GSMAP_SPOTS_PER_CHUNK="${GSMAP_SPOTS_PER_CHUNK}"

export OMP_NUM_THREADS="${GSMAP_THREADS}"
export OPENBLAS_NUM_THREADS="${GSMAP_THREADS}"
export MKL_NUM_THREADS="${GSMAP_THREADS}"
export MKL_DOMAIN_NUM_THREADS="${GSMAP_THREADS}"
export NUMEXPR_NUM_THREADS="${GSMAP_THREADS}"
export NUMBA_NUM_THREADS="${GSMAP_THREADS}"
export TOKENIZERS_PARALLELISM=false
export MPLBACKEND=Agg

cd "${PROJECT_DIR}"
python "${PY_SCRIPT}"
EOF
