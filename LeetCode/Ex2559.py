from typing import List


def vowelStrings(words: List[str], queries: List[List[int]]) -> List[int]:

    vowels = {'a', 'e', 'i', 'o', 'u'}
    prefixSum = [0]
    total = 0
    for word in words:
        if word[0] in vowels and word[-1] in vowels:
            total += 1
        prefixSum.append(total)
        
    res = [prefixSum[r+1] - prefixSum[l] for l, r in queries]

    return res

    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    words = [True if x[0].lower() in vowels and x[-1].lower() in vowels else False for x in words]
    res = [words[l:r+1].count(True) for l, r in queries]
    return res
    """


words = ["aba","bcb","ece","aa","e"]
queries = [[0, 2], [1, 4], [1, 1]]
print(vowelStrings(words, queries))
