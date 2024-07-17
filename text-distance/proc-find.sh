#!/bin/bash

source p3/bin/activate

mkdir -p out

for d in "" "-d"; do
	for k in 10 100 ; do
		python3 h2s-find-similarities.py $d -k $k < h2s.annotations.train.json.tsv > out/h2s.similarities-k$k$d.train.json 2> out/h2s.debug-similarities-k$k$d.train.txt &
	done
done
wait
