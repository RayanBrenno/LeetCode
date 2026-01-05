from collections import deque
from typing import List


def highestPeak(isWater: List[List[int]]) -> List[List[int]]:

    q = deque()
    m, n = len(isWater), len(isWater[0])
    res = [[-1] * n for x in range(m)] 
    for x in range(m):
        for y in range(n):
            if isWater[x][y]:
                q.append((x, y))
                res[x][y] = 0
                
    while q:
        print(q)
        x, y = q.popleft()
        aux = res[x][y]
        neighbors = [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]
        
        for i, j in neighbors:
            if i < 0 or i == m or j < 0 or j == n or res[i][j] != -1:
                continue
            q.append((i, j))
            res[i][j] = aux + 1

    return res


isWater = [[0, 1], [0, 0]]
print(highestPeak(isWater))
