import langid

def identify_language(text):
    try:
        lang, _ = langid.classify(text)
        return lang
    except:
        return "unknown"

if __name__ == "__main__":
    import sys
    for line in sys.stdin:
        print(f"{identify_language(line.strip())}\t{line.strip()}")