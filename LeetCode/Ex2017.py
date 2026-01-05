from typing import List


def gridGame(grid: List[List[int]]) -> int:
    
    n = len(grid[0])
    res = float('inf')
    sumUp = sum(grid[0])
    sumDown = 0

    for x in range(n):
        sumUp -= grid[0][x]
        res = min(res, max(sumUp, sumDown))
        sumDown += grid[1][x]

    return res
    

grid = [[1,3,1,15],[1,3,3,1]]
print(gridGame(grid))
