# Primeiro ele soma todos os valores da matriz e verifica se dá pra dividir em duas partes iguais (se for ímpar, já retorna False). Depois define um alvo (target) que é metade dessa soma. Aí ele tenta “cortar” a matriz de duas formas: somando linha por linha (corte horizontal) e coluna por coluna (corte vertical). Se em algum momento a soma acumulada bater exatamente o target, significa que dá pra dividir a matriz em duas partes com soma igual, então retorna True. Se nenhum corte funcionar, retorna False.

from typing import List

def canPartitionGrid(self, grid: List[List[int]]) -> bool:
    total_sum = sum(sum(aux) for aux in grid)

    if total_sum % 2 == 1:
        return False

    target = total_sum / 2

    aux1 = 0
    for x in grid:
        aux1 += sum(x)
        if aux1 == target:
            return True

    aux2 = 0
    for x in zip(*grid):
        aux2 += sum(x)
        if aux2 == target:
            return True

    return False


grid = [[1, 2], [3, 4]]
print(canPartitionGrid(None, grid))