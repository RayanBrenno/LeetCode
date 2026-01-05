from typing import List


def prefixCount(words: List[str], pref: str) -> int:

    return sum([1 if x.find(pref) == 0 else 0 for x in words])

    """
    res = 0

    for x in words:
        res += 1 if x.find(pref) == 0 else 0

    return res
    """


words = ["pay", "attention", "practice", "attend"]
pref = "at"
print(prefixCount(words, pref))
