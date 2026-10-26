# A ideia é percorrer a matriz procurando células com "1" e, quando encontrar uma, incrementar ans e usar DFS para explorar toda a ilha conectada. Durante a busca, cada célula visitada é transformada em "0" para marcá-la como explorada, evitando contar a mesma ilha mais de uma vez. Assim, cada nova célula "1" encontrada pelo for principal representa uma nova ilha, e no final retornamos a quantidade total de ilhas.

from typing import List


def numIslands(self, grid: List[List[str]]) -> int:
    m, n = len(grid), len(grid[0])
    ans = 0

    def dfs(i, j):
        if i >= m or j >= n or i < 0 or j < 0 or grid[i][j] == "0":
            return 0
        grid[i][j] = "0"
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
        return x

    for x in range(m):
        for y in range(n):
            if grid[x][y] == "1":
                ans += 1
                dfs(x, y)

    return ans


grid = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
print(numIslands(None, grid))  # Output: 3
