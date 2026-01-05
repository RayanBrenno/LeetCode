from typing import List


def reverseString(s: List[str]) -> None:
    i, j = 0, len(s) - 1
    
    while i < j :
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1


s = ["A", " ", "m", "a", "n", ",", " ", "a", " ", "p", "l", "a", "n", ",", " ",
     "a", " ", "c", "a", "n", "a", "l", ":", " ", "P", "a", "n", "a", "m", "a"]
print(reverseString(s))
