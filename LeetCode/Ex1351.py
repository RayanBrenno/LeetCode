# O algoritmo explora o fato de que a matriz está ordenada de forma decrescente: os valores maiores ficam à esquerda e acima, enquanto os menores (negativos) ficam à direita e abaixo. Por isso, começamos pelo canto superior direito da matriz.
# Se o valor atual for negativo, sabemos que todos os elementos abaixo dele na mesma coluna também serão negativos, então somamos m - i ao total e movemos para a esquerda. Caso o valor seja maior ou igual a zero, descemos uma linha, pois os valores negativos estarão mais à direita.
# Assim, percorremos a matriz de forma eficiente, contando todos os números negativos em tempo O(m + n), como foi solicitado.
from typing import List
def countNegatives(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    i, j = 0, n - 1
    ans = 0
    while i < m and j >= 0:
        if grid[i][j] < 0:
            j -= 1
            ans += m-i
        else:
            i += 1

    return ans

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(countNegatives(grid))

