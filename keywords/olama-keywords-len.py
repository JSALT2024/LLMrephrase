def crop_words_chars(s, lim=120):
    if len(s) < lim:
        return [s]
    sw = s.split(" ")
    l = 0
    for i in range(len(sw)):
        l += len(sw[i])+1
        if l >= lim:
            break
    if sum(len(x) for x in sw[i:]) < 50:
        return [s]
    return [" ".join(sw[:i])] + crop_words_chars(" ".join(sw[i:]),lim=lim)


import ollama
#from langchain_community.llms import Ollama

import sys

def joinm(x):
    return ", ".join(x)


def process(text):
    messages=[
      {
        'role': 'system',
        'content': f'You are an AI assistant. Extract important word from the following sentence. Do not answer anything else.',
      },
      {
        'role': 'user',
        'content': f'Let the wrist do all the leading.'
      },
      {
        'role': 'assistant',
        'content': joinm(["wrist","leading"])
      },
      {
        'role': 'user',
        'content': f'Aerosols, spraying for bugs, spraying perfumes around the house, all those sort of things, these birds have very very sensitive upper repository tracts and so if you have any sort of aerosol it can irritate their lungs.'
      },

      {
          'role':'assistant',
          'content': joinm(['aerosols','spraying bugs','perfumes','sensitive','respiratory tracts','irritate','lungs'])
        
        },
      {
        'role': 'user',
        'content': f'{text}'
      },
    ]

    print("-",text,file=sys.stderr)
    response = ollama.chat(messages=messages,
        model="llama3:70b",
           )
    out = response['message']['content']
    print(out,file=sys.stderr)
    print(file=sys.stderr)
    return out

def merge_out(out):
    return ", ".join(out)

def post_process(line, words):
    for kw in words.split(", "):
        if kw.lower() not in line.lower():
            return False
    return True

def ruled_process(line):
    pass

for line in sys.stdin:
    out = []
    for l in crop_words_chars(line, lim=120):
        o = process(l)
        out.append(o)
    o = merge_out(out)
    if post_process(line,o):
        print(line.strip(), "OK",repr(o),flush=True,sep="\t")
    else:
        print(line.strip(), "WRONG",repr(o),flush=True,sep="\t")
