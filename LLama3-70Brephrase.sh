#!/bin/bash
#PBS -l select=1:ncpus=12:ngpus=4:mem=512gb:plzen=True
#PBS -l walltime=2:00:00
#PBS -N Llama3-70Brephrase
module load mambaforge
conda activate Llama_HF
cd /auto/brno2/home/javorek
python LLama3-70Brephrase.py