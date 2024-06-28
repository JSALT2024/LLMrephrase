import truecase
import sys

# apply truecasing on stdin, output stdout


# why dummy word: because truecase assumes sentences, but we give captions,
# sometimes in the middle of sentence. This is a hack to fix it.

def apply_truecasing(text):    # Add a dummy word at the beginning
	dummy_text = "it " + text    # Apply truecasing on this
	truecased = truecase.get_true_case(dummy_text, out_of_vocabulary_token_option="as-is")    # Remove the dummy word and any extra space
	result = truecased[3:].strip()    # Ensure the first character is uppercase if it's a letter
	return result

for l in sys.stdin:
	text = l.strip()
	out = apply_truecasing(text)
	print(out)
