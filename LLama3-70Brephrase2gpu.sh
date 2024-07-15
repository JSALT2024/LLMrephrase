#!/bin/bash
#PBS -q gpu@pbs-m1.metacentrum.cz
#PBS -l select=1:ncpus=6:ngpus=2:mem=64gb:cl_galdor=True
#PBS -l walltime=2:00:00
#PBS -N Llama3-70Brephrase2gpu
module load mambaforge
conda activate /auto/plzen1/home/javorek/.conda/envs/Llama_HF
cd /auto/brno2/home/javorek
python LLama3-70Brephrase2gpu.py