#!/bin/bash
#PBS -q gpu@pbs-m1.metacentrum.cz
#PBS -l select=1:ncpus=12:ngpus=4:mem=128gb:cl_galdor=True
#PBS -l walltime=2:00:00
#PBS -N Llama3-70Brephrase
module load mambaforge
conda activate /auto/plzen1/home/javorek/.conda/envs/Llama_HF
cd /auto/brno2/home/javorek
python LLama3-70Brephrase.py