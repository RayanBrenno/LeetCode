from typing import List


def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]

    for i in range(m - k + 1):
        for j in range(n - k + 1):
            
            aux_grid = [grid[x][y] for x in range(i, i + k) for y in range(j, j + k)]
            min_diff = float('inf')
            aux_grid.sort()

            for x in range(1, len(aux_grid)):
                if aux_grid[x] == aux_grid[x - 1]:
                    continue
                min_diff = min(min_diff, aux_grid[x] - aux_grid[x - 1])
                if min_diff == 1:
                    break

            if min_diff != float("inf"):
                ans[i][j] = min_diff

    return ans


grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 2
print(minAbsDiff(None, grid, k))
