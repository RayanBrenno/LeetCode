from typing import Counter


def rearrangeCharacters(s: str, target: str) -> int:
    countS = Counter(s)
    countTarget = Counter(target)
    aux = []
    for char, num in countS.items():
        if char in target:
            aux.append(num//countTarget[char])
    
    return min(aux) if len(aux) == len(countTarget) else 0


s = "abc"
target = "abcd"
print(rearrangeCharacters(s, target))
