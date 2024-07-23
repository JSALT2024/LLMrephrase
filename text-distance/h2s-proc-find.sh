#!/bin/bash


mkdir -p out

for d in "" "-d"; do  # debug mode no and yes
	for k in 10 100 ; do  # 10 and 100 sents.
		# p3 is virtualenv with all the dependencies
		cmd="p3/bin/python3 h2s-find-similarities.py $d -k $k < h2s.annotations.train.json.tsv > out/h2s.similarities-k$k$d.train.json 2> out/h2s.debug-similarities-k$k$d.train.txt "
		# qsubmit runs the cmd on cluster with slurm . Works on ufal cluster.
		# https://github.com/ufal/qsubmit
		qsubmit -mem=10g -jobname=sim -logdir=logs "$cmd"
	done
done
wait
