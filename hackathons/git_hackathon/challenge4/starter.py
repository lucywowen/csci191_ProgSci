import sys

def top_n_words(filepath, n):
    """Return the top-n most common words in the given file.

    BUGS: this implementation is incomplete and does not normalize text.
    """
    counts = {}
    with open(filepath, "r") as f:
        for line in f:
            words = line.split()  # TODO: lowercase, strip punctuation
            for w in words:
                if w in counts:
                    counts[w] = counts[w] + 1
                else:
                    counts[w] = 1

    # BUG: not actually selecting top-n correctly
    items = list(counts.items())
    return items[:n]

def main():
    if len(sys.argv) < 3:
        print("Usage: python starter.py <input.txt> <N>")
        sys.exit(1)

    path = sys.argv[1]
    try:
        n = int(sys.argv[2])
    except ValueError:
        print("N must be an integer")
        sys.exit(1)

    top_words = top_n_words(path, n)
    print("Top words:")
    for word, count in top_words:
        print(word, count)

if __name__ == "__main__":
    main()
