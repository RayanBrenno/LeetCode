# A ideia é percorrer a matriz procurando células com valores maiores que zero e, quando encontrar uma, usar DFS para explorar toda a ilha conectada, somando os valores de suas células. Para evitar contar a mesma célula várias vezes ou processar a mesma ilha novamente, cada célula visitada é transformada em zero, marcando-a como já explorada. Ao terminar de percorrer a ilha, verificamos se a soma total é divisível por k e, caso seja, incrementamos ans.


from typing import List


def countIslands(self, grid: List[List[int]], k: int) -> int:
    m, n = len(grid), len(grid[0])
    ans = 0

    def dfs(i, j):
        if i >= m or j >= n or i < 0 or j < 0 or grid[i][j] == 0:
            return 0

        x = grid[i][j]
        grid[i][j] = 0
        x += dfs(i+1, j)
        x += dfs(i-1, j)
        x += dfs(i, j+1)
        x += dfs(i, j-1)
        return x

    for x in range(m):
        for y in range(n):
            if grid[x][y] > 0 and dfs(x, y) % k == 0:
                ans += 1

    return ans


grid = [[1, 2, 0], [0, 3, 4], [5, 0, 6]]
k = 3
print(countIslands(None, grid, k))  # Output: 2