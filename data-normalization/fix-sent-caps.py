#!/usr/bin/env python3

# Pá čen 28 17:48:02 CEST 2024

# we forgot to apply this step

import sys
vid = None
prev_eos = False
for line in sys.stdin:
	beg, dur, v, a,b,c,text = line.split("\t")

	if v == vid and prev_eos:
		text = text.capitalize() 
	prev_eos = text.strip()[-1] in ".?!"
	vid = v
	print(beg, dur, v, a,b,c,text,end="",sep="\t")



	
