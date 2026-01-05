from typing import Counter


def minimumLength(s: str) -> int:

    res = 0
    count = Counter(s)
    for x in count.values():
        res += 1 if x % 2 == 1 else 2 
    
    return res

s = "abaacbcbb"
print(minimumLength(s))