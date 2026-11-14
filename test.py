def concatenated_fibonacci(n_terms: int) -> str:
    """generate n_terms of concatenated fibonacci."""
    a, b = 0, 1
    result = []
    for _ in range(n_terms):
        result.append(str(a))
        a, b = b, a + b
    return "".join(result)

def canonical_encoding(seq) -> str:
    """canonically encode sequence via first occurrence labelling."""
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    labels = {}
    pattern = []
    for item in seq:
        if item not in labels:
            labels[item] = ALPHABET[len(labels)]
        pattern.append(labels[item])
    return "".join(pattern)

def find_excerpt(words: list[str], digits: str) -> list[int]:
    """find excerpt of words (structurally) in sequence of digits."""
    target = canonical_encoding(words)
    m = len(target)
    matches = []
    for start in range(len(digits) - m + 1):
        window = digits[start:start + m]
        if canonical_encoding(window) == target:
            matches.append(start)
    return matches

if __name__ == "__main__":
    excerpt = "lips sweat teeth lips spread teeth lips drip deep deep sweat skin".split()
    hits = find_excerpt(excerpt, concatenated_fibonacci(10000))
    print(hits)
