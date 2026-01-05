from typing import Counter


def longestPalindrome(s: str) -> str:
    if len(s) <= 1:
        return s
    aux = s[0]
    n = len(s)
    counter = Counter(s)
    for x in range(n):
        if counter[s[x]] < 2:
            continue

        for y in range(x+1, n):
            if s[x] == s[y]:
                aux2 = s[x:y+1]
                if aux2 == aux2[::-1] and len(aux2) > len(aux):
                    aux = aux2

        counter[s[x]] -= 1

    return aux

s = "babad"
print(longestPalindrome(s))
