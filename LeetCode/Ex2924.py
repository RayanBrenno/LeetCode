from collections import defaultdict


def findChampion(n, edges):
    
    count = [0] * n
    
    for _, x in edges:
        count[x] +=1
        
    res = []
    for index, value in enumerate(count):
        if value == 0:
            res.append(index)
        
    return res[0] if len(res) == 1 else -1
            
    
    
    """
    count = defaultdict(int)

    for x in range(n):
        count[x] = 0

    for _, x in edges:
        count[x] += 1

    count = sorted(count.items(), key=lambda item: item[1])
    
    return count[0][0] if count[0][1] != count[1][1] else -1
    """

n = 3
edges = [[2, 0], [2, 1]]
print(findChampion(n, edges))
