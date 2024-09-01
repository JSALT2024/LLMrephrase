import sys

with open("remove-langid.txt","r") as f:
	toremove = set([x.strip() for x in f.readlines()])

for line in sys.stdin:
	tabs = line.split("\t")
#	print(tabs)
	if tabs[2] in toremove:
		print(line,end="",file=sys.stderr)
		continue
	print(line,end="")
