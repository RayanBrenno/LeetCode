# Percorre a matriz contando quantos 1 cada linha possui e salva junto com o índice da linha em aux. Depois ordena essa lista para deixar as linhas mais fracas (menos soldados) primeiro. Por fim, percorre aux, adiciona os índices das k primeiras linhas em ans e retorna o resultado.

from typing import List


def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    aux = []
    for x, y in enumerate(mat):
        aux.append((y.count(1), x))

    aux.sort()
    ans = []
    for _, y in aux:
        if len(ans) < k:
            ans.append(y)
        else:
            break
    return ans
