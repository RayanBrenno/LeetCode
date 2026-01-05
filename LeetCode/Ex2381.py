from typing import List


def shiftingLetters(s: str, shifts: List[List[int]]) -> str:
    prefixDiff = [0] * (len(s)+1)
    
    for start, end, direction in shifts:
        prefixDiff[end + 1] += 1 if direction else -1
        prefixDiff[start] += -1 if direction else 1
    
    aux = 0
    res = [ord(x) - ord("a") for x in s]
    
    for x in reversed(range(len(prefixDiff))):
        aux += prefixDiff[x]
        res[x-1] = (aux + res[x-1]) %26 
    
    s = [chr(ord("a") + x) for x in res]
    
    return "".join(s)


s = "abc"
shifts = [[0, 1, 0], [1, 2, 1], [0, 2, 1]]
print(shiftingLetters(s, shifts))
