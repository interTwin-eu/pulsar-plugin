#!/bin/bash

## general configuration of the job
#SBATCH --job-name=itwinai-radio-astronomy
#SBATCH --account=intertwin
#SBATCH --mail-user=
#SBATCH --mail-type=ALL
#SBATCH --output=report.out
#SBATCH --error=progress.out
#SBATCH --time=00:10:00

## configure node and process count on the CM
#SBATCH --partition=devel
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=48
#SBATCH --exclusive

ml --force purge
ml Stages/2024 Python/3.11

source .venv/bin/activate
pytest -s tests 