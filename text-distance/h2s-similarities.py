from sentence_transformers import SentenceTransformer
import sys
import numpy as np

# by Dominik
# code originally taken here: https://www.sbert.net/docs/sentence_transformer/pretrained_models.html

# Usage: python3 h2s-similarities.py < text 

# - text must be one sentence per line
# - outputs are saved to npy files
# - How2Sign train runs 1m28s on 16g RAM GPU, needs 1.2G memory

np.set_printoptions(threshold=np.inf)

mname="all-mpnet-base-v2"

# 1. Load a pretrained Sentence Transformer model
model = SentenceTransformer(mname,device="cuda")
print("model loaded")

# The sentences to encode
sentences = [x.strip() for x in sys.stdin.readlines()]
print("sentences loaded")
# 2. Calculate embeddings by calling model.encode()
embeddings = model.encode(sentences,batch_size=32)

e = np.asarray(embeddings,dtype=np.float16)
print("embeddings counted")

np.save("h2strain.npy",e)
print("embeddings saved")
# [3, 384]

# 3. Calculate the embedding similarities
similarities = model.similarity(embeddings, embeddings)
print("similarities counted")
s = np.asarray(similarities,dtype=np.float16)
print("similarities saved")
# tensor([[1.0000, 0.6660, 0.1046],
#         [0.6660, 1.0000, 0.1411],
#         [0.1046, 0.1411, 1.0000]])
