from typing import Counter


def canConstruct(s: str, k: int) -> bool:
    if k > len(s):
        return False
    
    count = Counter(s)
    aux = 0
    
    for x in count.values():
        aux += x % 2
    
    return aux <= k


s = "annabelle"
k = 2
print(canConstruct(s, k))