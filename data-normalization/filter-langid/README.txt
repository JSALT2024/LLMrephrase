langid-data.tsv
lang_id.py


remove-langid.txt
	- the videoids to remove because they contain <= 25% of captions
	  detected as not English. We expected them.


stats-x.py
	- makes statistics about language id

filter-langid.py
	- takes the train norm tsv file, opens remove-langid.txt and produces
	  the non-filtered ones

