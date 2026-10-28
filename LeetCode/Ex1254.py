# A ideia é percorrer a matriz procurando células com valor 0 e usar DFS para explorar toda a ilha, marcando as células visitadas como 1 para não contar a mesma ilha novamente. Durante a exploração, verificamos se algum caminho ultrapassa os limites da matriz, o que significa que a ilha toca a borda e não é fechada. O DFS retorna True apenas quando todos os caminhos permanecem dentro da matriz e encontram água, então incrementamos ans somente quando a ilha inteira está cercada por 1 em todas as direções.


from typing import List


def closedIsland(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    ans = 0

    def dfs(i, j):
        if i >= m or j >= n or i < 0 or j < 0:
            return False

        if grid[i][j] == 1:
            return True

        grid[i][j] = 1

        right = dfs(i + 1, j)
        left = dfs(i - 1, j)
        up = dfs(i, j + 1)
        down = dfs(i, j - 1)

        return right and left and up and down

    for x in range(m):
        for y in range(n):
            if grid[x][y] == 0:
                if dfs(x, y):
                    ans += 1

    return ans


grid = [[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [
    1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0]]
print(closedIsland(None, grid))
