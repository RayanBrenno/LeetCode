from typing import List


def stringMatching(words: List[str]) -> List[str]:
    aux = " ".join(words)

    res = [i for i in words if aux.count(i) >= 2]


    return res

    """
    res = set()

    for x in range(len(words)):
        for y in range(len(words)):
            if words[x] in words[y] and y != x:
                res.add(words[x])

    return list(res)
    """


words = ["leetcoder", "leetcode", "od", "hamlet", "am"]
print(stringMatching(words))
