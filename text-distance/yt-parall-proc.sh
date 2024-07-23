#!/bin/bash

infile=yt.annotations.train.json.tsv

n=$(wc -l < $infile)
packs=320  # process 320 sentences in one process
BS=32  # batch size
mkdir -p packs  # dir where it will be saved


# 1. uncomment this, comment the next for loop, then run this, wait until everything is done
#for i in `seq 0 $packs $n` ; do
#	from=$i
#	to=$(($i+$packs))
#	cmd="cat $infile | p3/bin/python3 yt-find-similarities.py -k 100 -b $BS -d --beg $from --end $to > packs/out.$from.$to.json && touch packs/out.$from.$to.json.ok"
#	qsubmit --mem=16g --cpus=1 --jobname p$from --logdir=plogs "$cmd"
#done


# 2. comment the previous for loop, uncomment and run this
for i in `seq 0 $packs $n` ; do
	from=$i
	to=$(($i+$packs))

	# check if everything is ok. If not, process again
	if [ ! -f packs/out.$from.$to.json.ok ]; then
		cmd="cat $infile | p3/bin/python3 yt-find-similarities.py -k 100 -b $BS -d --beg $from --end $to > packs/out.$from.$to.json && touch packs/out.$from.$to.json.ok"
	#	qsubmit --mem=16g --cpus=1 --jobname p$from --logdir=plogs "$cmd"
		echo "$cmd"
	fi
	echo packs/out.$from.$to.json  # if it's ok, merge the jsons into one
done | python3 merge-jsons.py > yt.similarities-100-d.json
