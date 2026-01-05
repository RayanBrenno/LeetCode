from collections import deque
from typing import List


def islandPerimeter(grid: List[List[int]]) -> int:
    res = 0
    m, n = len(grid), len(grid[0])
    for x in range(m):
        for y in range(n):
            if grid[x][y] == 1:
                neighbors = [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]
                for i, j in neighbors:
                    if i < 0 or j < 0 or i == m or j == n:
                        res+=1
                        continue 
                    if 0 <= i < m and 0 <= j < n and grid[i][j] == 0:
                        res += 1
    return res


grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
print(islandPerimeter(grid))
