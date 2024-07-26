#!/usr/bin/env python3
import json
import sys

from mosestokenizer import MosesTokenizer

tokenizer = MosesTokenizer('en')

def tokenize(text):
    return tokenizer.tokenize(text)

def lowtokenize(text):
    return [l.lower() for l in tokenize(text)]

def inters(a,b):
    i = set(a).intersection(set(b))
    return len(i)

def interscount(a,b):
    sa = [x for x in a ]
    i = 0
    for w in b:
        if w in sa:
            i += 1
            sa.pop(sa.index(w))
    return i

data = json.load(sys.stdin)

for k,d in data.items():
    t = d["translation"]
    t_tok = lowtokenize(t)

    d["_translation_lowtokens"] = t_tok
    for which in ["positive","negative"]:
        d[f"_{which}_text_lowtokens"] = []
        d[f"_{which}_tokens_intersection"] = []
        print(t_tok,file=sys.stderr)
        for pt in d[f"_{which}_text"]:
            pt_tok = lowtokenize(pt)
            i = interscount(t_tok, pt_tok)
            d[f"_{which}_text_lowtokens"].append(pt_tok)
            d[f"_{which}_tokens_intersection"].append(i)
            print(i,pt_tok,file=sys.stderr,sep="\t")
#    print(d)

#    print(t)
json.dump(data,sys.stdout,indent=4)
