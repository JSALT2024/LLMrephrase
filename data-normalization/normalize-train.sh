#!/bin/bash

# input files meant to be present in this directory

# this one to be downloaded from http://ufallab.ms.mff.cuni.cz/~machacek/jsalt24-slt/youtube-asl/train.filtered3.beg_dur_id_frames_fps_text.tsv
INFILE=train.filtered3.beg_dur_id_frames_fps_text.tsv

# this file contains the video ids of the documents to truecase
to_truecase=ids-to-truecase.txt


# split $INFILE to truecase and not
if false; then  # change to true to do it again
	: > train_to_truecase
	: > train_not_to_truecase

	cat $INFILE | while read line; do 
		vid=$(echo "$line" | cut -f 3)
		echo $vid
		if grep "^$vid" $to_truecase; then
			echo "$line" >> train_to_truecase
		else
			echo "$line" >> train_not_to_truecase
		fi
	done
fi


if false; then
#if true; then
	cut -f 7 train_to_truecase | ./our-normalize.sh | p3/bin/python3 apply_truecase.py | sed 's/ \././g' > train_to_truecase.norm.tc &
	cut -f 7 train_not_to_truecase | ./our-normalize.sh > train_not_to_truecase.norm
	wait
fi

paste <( cut -f 1-6 train_to_truecase ) train_to_truecase.norm.tc > ts.train_to_truecase.norm.tc
paste <( cut -f 1-6 train_not_to_truecase ) train_to_truecase.norm.tc > ts.train_not_to_truecase.norm

# create the final norm file
cat ts.train_not_to_truecase.norm ts.train_to_truecase.norm.tc > train.filtered3.beg_dur_id_frames_fps_text.norm.tsv

