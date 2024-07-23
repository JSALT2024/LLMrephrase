#!/bin/bash

# testing what batch size takes what time on GPU
# Beware that it's running on random GPU type that's available for the job. 
# It seemed like 4096 has the fastest time per sentence

#for bs in 1 8 16 32 64 128 256 512 1024 ; do
for bs in 2048 4096 8192 16384; do
	cmd="time cat ../yt.annotations.train.json.tsv | ../p3/bin/python3 yt-find-similarities.py -k 1 -b $bs --end $bs > out-$bs.json "
	qsubmit -gpus=1 -mem=20g "$cmd" -jobname=bs$bs
done

