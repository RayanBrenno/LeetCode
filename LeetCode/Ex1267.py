from typing import List
from collections import deque


def countServers(grid: List[List[int]]) -> int:

    res = 0
    rows, cols = len(grid), len(grid[0])
    rowsCount = [0] * rows
    colsCount = [0] * cols
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                rowsCount[row] += 1
                colsCount[col] += 1

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1 and (rowsCount[row] > 1 or colsCount[col] > 1):
                res += 1

    return res


grid = [[1, 0, 0, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0]]
for x in grid:
    print(x)
print(countServers(grid))
