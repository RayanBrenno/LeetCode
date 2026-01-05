from collections import defaultdict
from typing import List


def substringXorQueries(s: str, queries: List[List[int]]) -> List[List[int]]:

    dic = defaultdict(list)
    for i in range(1, 31):
        for j in range(len(s)-i+1):
            if s[j] == '1' or i == 1:
                if int(s[j:j+i], 2) not in dic:
                    dic[int(s[j:j+i], 2)] = [j, j+i-1]
                    
    res = []    
    for x, y in queries:
        if x ^ y in dic:
            res.append(dic[x ^ y])
        else:
            res.append([-1, -1])
    return res

    """
    n = len(queries)
    res = [[-1,-1]]*n
    for x in range(n):
        val = queries[x][0] ^ queries[x][1] 
        binary = bin(val)[2:]
        if binary in s:
            aux = s.find(binary)
            res[x] = [aux, aux+len(binary)-1]

    return res
    """


s = "101101"
queries = [[0, 5], [1, 2], [12, 8]]
print(substringXorQueries(s, queries))
