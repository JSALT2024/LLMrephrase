#!/bin/bash
# by Dominik

# take text stdin, one caption at each line, and normalize it with following
# steps (in each pipe)

# 1. HTML unescape  -- there is sometimes &amp; meant as & . Similarly with
# > and <

# 2.-3:
# perl remove-non-printing-char.perl | perl normalize-punctuation.perl -l en 
# scripts from moses. We got them from here:
# https://github.com/browsermt/students/blob/36cf85a94aa19edaf37afe97722e0e90fd5dc524/train-student/clean/clean-mono.sh#L22C60-L22C151
# because it was used in dissertation of Jindřich Helcl. 
# It's SOTA in # MT. 

sed 's/\&amp;/\&/g;s/\&gt;/>/g;s/\&lt;/</g' | perl remove-non-printing-char.perl | perl normalize-punctuation.perl -l en 

