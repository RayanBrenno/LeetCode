# Esse exercício calcula, para cada posição da matriz, a diferença entre a quantidade de 1s e 0s na linha e na coluna. Primeiro ele pega o tamanho da matriz (m e n). Depois calcula ones_row, que guarda quantos 1 existem em cada linha, usando sum(row), e ones_col, que guarda quantos 1 existem em cada coluna, usando zip(*grid) para transpor a matriz e somar cada coluna. No final, ele monta a matriz resposta usando list comprehension, aplicando a fórmula 2*row + 2*col - m - n, que vem da simplificação de (onesRow + onesCol - zerosRow - zerosCol). Assim ele calcula o valor de cada célula de forma direta e retorna a nova matriz.

from typing import List


def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:

    m, n = len(grid), len(grid[0])

    ones_row = [sum(row) for row in grid]
    ones_col = [sum(col) for col in zip(*grid)]

    return [[2*row + 2*col - m - n for col in ones_col] for row in ones_row]

    # m, n = len(grid), len(grid[0])
    # ones_row = [0] * m
    # ones_col = [0] * n

    # for x in range(m):
    #     for y in range(n):
    #         if grid[x][y] == 1:
    #             ones_row[x] += 1
    #             ones_col[y] += 1

    # ans = [[0]*n for _ in range(m)]

    # for x in range(m):
    #     for y in range(n):
    #         ans[x][y] = ones_row[x] + ones_col[y] - \
    #             (m-ones_row[x]) - (n-ones_col[y])

    # return ans


grid = [[0, 1, 1], [1, 0, 1], [0, 0, 1]]
print(onesMinusZeros(None, grid))
