#!/usr/bin/env python3
import json
import sys

# remove duplicate clipids from yt.annotations.train.json on stdin
# outputs the new version to stdout

data = json.load(sys.stdin)
for k in data.keys():
    cl = data[k]["clip_order"]
    o = [cl[0]]
    for i in range(1,len(cl)):
        if cl[i] not in o:
            o.append(cl[i])
    data[k]["clip_order"] = o
json.dump(data,sys.stdout,indent=4)
        
        
