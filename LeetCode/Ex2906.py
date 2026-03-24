# Esse exercício constrói uma nova matriz onde cada posição contém o produto de todos os elementos da matriz original exceto o próprio elemento, usando módulo 12345. Para evitar divisão (e lidar com zeros), ele usa a ideia de prefixo e sufixo. Primeiro, percorre a matriz de trás pra frente calculando um produto acumulado (suffix), armazenando em cada posição o produto de todos os elementos à frente. Depois, percorre da frente pra trás com outro acumulador (prefix), multiplicando o valor atual pelo produto de todos os elementos anteriores. No final, cada célula acaba contendo o produto de todos os outros elementos da matriz, tudo feito de forma eficiente e sem precisar recalcular produtos repetidamente.

from typing import List

def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
    mod = 12345
    n, m = len(grid), len(grid[0])
    p = [[0] * m for _ in range(n)]

    suffix = 1
    for x in range(n -1, -1, -1):
        for y in range(m - 1, -1, -1):
            p[x][y] = suffix 
            suffix = (suffix * grid[x][y]) % mod

    prefix = 1
    for x in range(n):
        for y in range(m):
            p[x][y] = (p[x][y] * prefix) % mod
            prefix = (prefix * grid[x][y]) % mod

    return p


grid = [[1,2,3],[4,5,6],[7,8,9]]
print(constructProductMatrix(None, grid))