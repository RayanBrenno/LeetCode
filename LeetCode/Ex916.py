from typing import Counter, List


def wordSubsets(words1: List[str], words2: List[str]) -> List[str]:
    counter = Counter()
    for word in words2:
        curCounter = Counter(word)
        for key in curCounter:
            counter[key] = max(counter[key], curCounter[key])

    res = []
    for word in words1:
        curCounter = Counter(word)
        if all(curCounter[key] >= counter[key] for key in counter):
            res.append(word)

    return res  


words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["lo", "eo"]
print(wordSubsets(words1, words2))
