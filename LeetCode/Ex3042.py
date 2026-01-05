from typing import List


def countPrefixSuffixPairs(words: List[str]) -> int:

    res = 0

    for i in range(len(words)):
        for j in range(i+1, len(words)):
            aux1, aux2 = words[i], words[j]
            print(f"{i=}, {j=}")
            if aux2.startswith(aux1) and aux2.endswith(aux1):
                print("entrou")
                res += 1

    return res


words = ["a", "aba", "ababa", "aa"]
print(countPrefixSuffixPairs(words))