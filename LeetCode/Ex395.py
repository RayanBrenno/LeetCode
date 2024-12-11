from collections import defaultdict


def longestSubstring(s: str, k: int) -> int:

    dic = defaultdict(int)
    biggest = 0
    for x in s:
        dic[x] += 1

        if max(dic.values()) > k:
            biggest = max(biggest, sum(dic.values()))
            dic = defaultdict(int)
    biggest = max(biggest, sum(dic.values()))
    return biggest


s = "aabbb"
k = 2
print(longestSubstring(s, k))
