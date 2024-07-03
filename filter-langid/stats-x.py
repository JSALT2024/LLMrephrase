import sys

ids = {}

for line in sys.stdin:
	vid, lan = line.split()
	if vid not in ids:
		ids[vid] = [0,0]
	if lan == "en":
		i = 0
	else:
		i = 1
	ids[vid][i] += 1


proportion = []

for v in ids.keys():
	t = (ids[v][0]/(ids[v][0]+ids[v][1]), v, *ids[v])
	proportion.append(t)

with open("remove-langid.txt","w") as f:
	for x in sorted(proportion,key=lambda x:x[0]):
		if x[0] <= 0.25:
			print(x[1],file=f)
		print(*x)
