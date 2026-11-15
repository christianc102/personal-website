---
title: concatenated fibonacci
published: true
math: true
---

I recently read Kaveh Akbar's *Martyr!*, in which the protagonist Cyrus Shams is a young poet. In a memorable vignette into his day-to-day life, Akbar describes the creative process of Cyrus preparing an "experimental piece" for a local open mic:

> assigning words to each digit 0-9, then using an Excel document to generate a lyric out of those words as the digits appeared in the Fibonacci sequence: "lips sweat teeth lips spread teeth lips drip deep deep sweat skin," etc.

I loved the creativity of the idea but the pattern itself gave me pause: did Akbar actually use this process in generating the snippet? If he did, could we infer the word-digit mapping, and, if he didn't, could we prove it[^1]? 

Let's investigate!

---

To start, we can think about digit appearance by defining the concatenated Fibonacci sequence, formed by infinitely gluing successive terms of the traditional Fibonacci sequence together[^2], as follows:

> 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ... → 01123581321345589...

Formalizing the problem, we're given an infinite digit sequence $$S$$ as defined above, the observed excerpt of words $$E$$, and an unknown mapping[^3]

$$
f: \{0,1,2,\dots,9\} \to \{\text{set of words}\}.
$$

With this formulation, the problem can then be recast as a substring search, where the goal is to determine whether (and where) $$f^{-1}(E)$$[^4] occurs in $$S$$ for all possible $$f$$. The naive exhaustive approach would conduct this substring search for all possible word-digit mappings $$f$$. 

In the provided excerpt, the unique words are: ['lips', 'sweat', 'teeth', 'spread', 'drip', 'deep', 'skin'], which implies there are $$P(10, 7) = 10! / 3! = 604{,}800$$ possible word assignments of the digits 0-9 to the set of seven unique words. 

While this is certainly doable computationally, it's not the cleanest approach.

We can instead observe a key point: we don't actually need to know $$f$$ to search the substring! In the observed excerpt $$E$$, the pattern of which positions repeat is preserved under any injective mapping $$f$$, and if we encode both the observed excerpt and concatenated Fibonacci sequence via a consistent rule, we can look for occurrences irrespective of our (or I suppose, Cyrus's) choice of $$f$$. 

Therefore, our algorithm involves relabelling the excerpt and every sliding window substring of length $$m=12$$ by first appearance, i.e. "lips sweat teeth lips spread teeth lips drip deep deep sweat skin" becomes "ABCADCAEFFBG" and 011235813213 becomes "AABCDEACBACF".

The Python code is then simple:

```python
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

excerpt = "lips sweat teeth lips spread teeth lips drip deep deep sweat skin".split()
hits = find_excerpt(excerpt, concatenated_fibonacci(10000))
print(hits)
```

We find that the first match occurs at index 3,198,014! Here, the 12 digit sequence is 271251230074, which gives the mapping lips=2, sweat=7, teeth=1, spread=5, drip=3, deep=0, skin=4. This match starts inside the digit representation of $$F_{5531}$$. Therefore, it seems extremely unlikely that Cyrus really generated 5531 elements of the sequence before deciding to commence his poem[^5], so we can conclude that Akbar likely **did not** use this process to generate the snippet.

---

This is all in good fun! Frankly, it would have been quite a surprising result to discover that Akbar actually used the process outlined to create the snippet. It seems he dedicated his time elsewhere, instead focusing on crafting a beautiful and imaginative novel? I guess we'll never know :).

[^1]: Given that the concatenated Fibonacci sequence is infinite, we can't *prove* that he didn't, but we can at least try to find the earliest occurrence of the pattern (which also gives us an approximate upper bound on the likelihood Akbar actually carried out the process, haha!). 

[^2]: We adopt the convention of starting the Fibonacci sequence with $$F_0 = 0$$. 

[^3]: We assume that the map $$f$$ is injective, i.e. two digits do not share a word. 

[^4]: Apologies for the ugly / overloaded notation: the idea is to map the observed excerpt of words back to their original numbers and this seemed to me to be a more concise way to express this without sacrificing too much clarity.

[^5]: And even worse, he wouldn't have been able to do this in Excel, since Excel only stores 15 significant digits, thus limiting his generation to $$F_{73}$$.