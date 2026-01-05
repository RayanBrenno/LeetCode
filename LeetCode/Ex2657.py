from typing import Counter, List


def findThePrefixCommonArray(a: List[int], b: List[int]) -> List[int]:
    n = len(a)
    res = []
    aux = [0] * (n + 1)
    count = 0

    for x in range(n):
        if aux[a[x]] == 0:
            aux[a[x]] = 1
        elif aux[a[x]] == 1:
            count += 1
        if aux[b[x]] == 0:
            aux[b[x]] = 1
        elif aux[b[x]] == 1:
            count += 1
        res.append(count)
        
    return res

    """
    res = []
    count = Counter()
    
    for a, b in zip(a, b):
        count[a] +=1
        count[b] +=1
        res.append(sum(1 for x in count.values() if x == 2))
    
    return res
    """


a = [1, 3, 2, 4]
b = [3, 1, 2, 4]
print(findThePrefixCommonArray(a, b))
