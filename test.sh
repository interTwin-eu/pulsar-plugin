#!/bin/bash

## general configuration of the job
#SBATCH --job-name=itwinai-radio-astronomy
#SBATCH --account=slfse
#SBATCH --partition=devel
#SBATCH --output=output.out
#SBATCH --error=error.out
#SBATCH --time=00:10:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=48
#SBATCH --exclusive

ml --force purge
ml Stages/2024  GCCcore/.12.3.0 Python/3.11.3

source /p/project1/intertwin/krochak1/pulsar-plugin/.venv-juwels/bin/activate

cd /p/project1/intertwin/krochak1/pulsar-plugin
pytest -s tests 