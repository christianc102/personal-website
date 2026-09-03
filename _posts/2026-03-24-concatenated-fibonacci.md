---
title: concatenated fibonacci
published: false
---

I was recently reading *Martyr* by Kaveh Akbar, in which the main character Cyrus Shams is a young poet. In a memorable vignette into his day-to-day life, he describes presenting an "experimental piece" at a local open mic. His creative process is described as follows:

> assigning words to each digit 0-9, then using an Excel document to generate a lyric out of those words as the digits appeared in the Fibonacci sequence: "lips sweat teeth lips spread teeth lips drip deep deep sweat skin," etc.

I marvelled at the creativity of the idea but continued reading. However, I couldn't dismiss a few nagging questions: did Akbar actually use this process in generating the snippet? If he did, could we infer the word-digit mapping, and, if he didn't, could we prove it? 

Let's investigate:

--

To start, we can think about digit appearance by defining the concatenated Fibonacci sequence, formed by gluing infinite successive terms of the traditional Fibonacci sequence together, as follows:

> 1, 1, 2, 3, 5, 8, 13, 21, 34, ... → 1123581321345589...

With this formulation, the problem can then be recast as a substring search, and the naive exhaustive approach would conduct this substring search for all possible word-digit mappings. 

In the provided excerpt, the unique words are: ['lips', 'sweat', 'teeth', 'spread', 'drip', 'deep', 'skin'], which implies there are 10! / 3! = 604,800 possible word assignments from the set of unique words to the digits 0-9. 

While this is certainly doable computationally, it's not the cleanest approach.

[to be continued]