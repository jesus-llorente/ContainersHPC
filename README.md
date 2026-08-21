# Singularity/Apptainer Course

## Chapter 1 — Foundations
Why Docker doesn't work on shared HPC clusters (root daemon requirement), rootless design of Singularity/Apptainer, JEX setup (`module load singularityce`, `$SINGULARITY_CACHEDIR`).

## Chapter 2 — Build & Run
`.def` file structure (Bootstrap, From, %files, %post, %runscript), building via `--remote` (Sylabs) or `--fakeroot`, `.sif` single-file image format, `run`/`exec`/`shell` subcommands.

## Chapter 3 — Data & Reproducibility
Bind mounts (`--bind`, `$SINGULARITY_BIND`), auto-bound paths (`$HOME`, `$PWD`), pinning exact dependency versions in the `.def` for long-term reproducibility.

## Chapter 4 — Running on Slurm
`sbatch` script structure, resource requests (CPU/mem/walltime), calling `singularity exec` inside a batch job instead of interactively, `--nv` for GPU jobs.

## Chapter 5 — Polish & Demo
Multi-step pipelines as one script or a job array, README for reproducing the run on JEX, explaining *why* each design choice was made — the part that actually gets tested in an interview.