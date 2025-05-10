#!/bin/sh
#SBATCH --job-name=make_bandpass_speech
#SBATCH --time=0-5:0:0
##SBATCH -n 1
#SBATCH --mem=2000
##SBATCH --nice=0

## 1-N array jobs % K jobs at a time
#SBATCH --array 1-61


learning_rate_idx="$SLURM_ARRAY_TASK_ID"
source activate tf2

python make_bandpass_speech.py $learning_rate_idx   -U