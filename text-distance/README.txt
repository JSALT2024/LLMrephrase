Most and least similar sentences by LLM-embedding score (BERTScore-like)

by Dominik


Install:

pip install sentence-transformers sklearn

json-to-tsv.py
	- symlink from https://github.com/JSALT2024/scripts/blob/main/csv_json_parsers/json-to-tsv.py , not commited again in this dir
	- use it to convert {yt,h2s}.annotations.{train,dev}.json to *.json.tsv . It is input format for the next scripts.

#  How2Sign:
############

h2s-similarities.py
	- self-documented
	- creates 
	- saves the embeddings and pair-wise similarities, if it has enough RAM
		- it creates numpy files: 
			- h2strain.npy ... the embeddings
			- h2strain_sim.npy ... the pair-wise similarities
	- it uses the all-mpnet-base-v2 model because sentence_transformers leaderboard suggests it's the best

h2s-find-similarities.py
	- self-documented
	- creates json

h2s-proc-find.sh
	- runs multiple versions in one script


# YT-ASL:
#########

yt-similarities.py
	- as h2s-similarities.py
	- creates: 
		- yttrain.npy ... the embeddings
		- attempts to create the yttrain_sim.py and fails on OOM. Don't worry, the next scripts work with the embeddings only.

yt-find-similarities.py
	- self-documented
	- counts the vector similarity and produces json

yt-parall-proc.sh
	- script to parallelize processing YT-ASL using yt-find-similarities.py
	- first it creates lots of small jsons...

merge-jsons.py
	- ...then it merges them with this


yt-gpu/
	- I run yt-asl once again in this dir, using yt-gpu/yt-parall-proc.sh
	
yt-gpu/remove-dubbed-clipids.py
	- removes duplicate clipids
	
