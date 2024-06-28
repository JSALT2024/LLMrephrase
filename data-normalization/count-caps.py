#!/usr/bin/env python3

# to be applied on train.filtered3.beg_dur_id_frames_fps_text.tsv
# it prints the statistics of casing for each videoid. Then inspect them
# elsewhere

import sys
import string
lower = 0
upper = 0
vid = None
maxt = 0
for line in sys.stdin:
	beg, dur, v, text = line.split("\t")
	beg = float(beg)
	dur = float(dur)
	if v != vid and vid is not None:
		n = lower+upper
		print(vid,upper/n, lower/n, lower, upper, maxt)

		lower = 0
		upper = 0
		vid = None
		maxt = 0

	for t in text:
		if t.isupper():
			upper += 1
		elif t in string.punctuation:
			pass
		elif t.isspace():
			pass
		else:
			lower += 1
	maxt = max(beg+dur, maxt)
	vid = v
n = lower+upper
print(vid,upper/n, lower/n, lower, upper, maxt)
