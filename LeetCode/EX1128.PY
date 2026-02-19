from typing import List

def numEquivDominoPairs(dominoes: List[List[int]]) -> int:
    dic = {}

    for x in dominoes:
        aux = tuple(sorted(x))
        if aux in dic:
            dic[aux] += 1
        else:
            dic[aux] = 1

    res = 0
    for x in dic.values():
        s = x*(x-1)//2
        res += s
    return res


dominoes = [[1, 2], [1,2],[1,1],[1,2],[2,2]]
print(numEquivDominoPairs(dominoes))
