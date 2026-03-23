# Esse código inverte verticalmente uma submatriz quadrada de tamanho k x k dentro da matriz grid, começando na posição (x, y). Ele usa dois ponteiros (i0 no topo e i1 na base da submatriz) e vai trocando as linhas correspondentes entre si, coluna por coluna, dentro do intervalo definido. A cada iteração, i0 sobe e i1 desce, até que eles se encontrem, garantindo que toda a submatriz seja invertida de cima para baixo. No final, a matriz modificada é retornada.

from typing import List

def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
    i0, i1 =  x, x + k - 1
    while i0 < i1:
        for j in range(y, y + k):
            grid[i0][j], grid[i1][j] = grid[i1][j], grid[i0][j]
        i0 += 1
        i1 -= 1
    return grid


grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
x = 1
y = 0
k = 3
print(reverseSubmatrix(None, grid, x, y, k))