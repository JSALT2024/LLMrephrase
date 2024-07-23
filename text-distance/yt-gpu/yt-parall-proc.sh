#!/bin/bash

# Comments: see ../yt-proc-parallel

infile=../yt.annotations.train.json.tsv

n=$(wc -l < $infile)
BS=4096
packs=$((20*$BS))
mkdir -p packs



#for i in `seq 0 $packs $n` ; do
#	from=$i
#	to=$(($i+$packs))
#	cmd="cat $infile | ../p3/bin/python3 yt-find-similarities.py -k 100 -b $BS -d --beg $from --end $to > packs/out.$from.$to.json && touch packs/out.$from.$to.json.ok"
#	qsubmit --mem=16g --gpus=1 --jobname p$from --logdir=plogs "$cmd"
#done
#
for i in `seq 0 $packs $n` ; do
	from=$i
	to=$(($i+$packs))
	if [ ! -f packs/out.$from.$to.json.ok ]; then
		cmd="cat $infile | p3/bin/python3 yt-find-similarities.py -k 100 -b $BS -d --beg $from --end $to > packs/out.$from.$to.json && touch packs/out.$from.$to.json.ok"
	#	qsubmit --mem=16g --cpus=1 --jobname p$from --logdir=plogs "$cmd"
		echo "$cmd"
	fi
	echo packs/out.$from.$to.json
done | python3 merge-jsons.py > yt.similarities-100-d.json
