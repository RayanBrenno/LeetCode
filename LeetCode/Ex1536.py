# Esse código resolve o problema contando o número mínimo de trocas de linhas necessárias para deixar a matriz válida. Primeiro, ele calcula para cada linha quantos zeros consecutivos existem no final e guarda isso na lista zeros. Depois, para cada posição i, ele determina quantos zeros aquela linha precisa ter no final (n - 1 - i). Em seguida, procura de baixo para cima a primeira linha que tenha pelo menos essa quantidade de zeros. Se não encontrar, retorna -1 porque é impossível organizar. Se encontrar, ele “puxa” essa linha até a posição correta fazendo trocas adjacentes e soma cada troca em ans. No final, retorna o total de swaps realizados.

from typing import List


def minSwaps(self, grid: List[List[int]]) -> int:
    ans = 0
    n = len(grid)
    zeros = []
    for x in grid:
        count = 0
        for i in range(n-1, -1, -1):
            if x[i] == 0:
                count += 1
            else:
                break
        zeros.append(count)
    for i in range(n):
        zeros_needed = n - 1 - i
        j = i
        while j < n and zeros[j] < zeros_needed:
            j += 1
        if j == n:
            return -1
        for k in range(j, i, -1):
            zeros[k], zeros[k-1] = zeros[k-1], zeros[k]
            ans += 1

    return ans


grid = [[1, 0, 0], [1, 1, 0], [1, 1, 1]]
print(minSwaps(None, grid))