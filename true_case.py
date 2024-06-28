import truecase

def apply_truecasing(text):
    return truecase.get_true_case(text)

if __name__ == "__main__":
    import sys
    for line in sys.stdin:
        print(apply_truecasing(line.strip()))

        