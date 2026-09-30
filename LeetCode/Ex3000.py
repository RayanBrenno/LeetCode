# A implementação percorre cada retângulo calculando `x² + y²`, que representa o quadrado da diagonal e permite compará-las sem precisar calcular a raiz. A cada retângulo, também calcula sua área e atualiza `ans` quando encontra uma diagonal maior. Caso a diagonal seja igual à maior já encontrada, mantém a maior área entre os dois retângulos. Ao final, retorna a área do retângulo com a maior diagonal.


from typing import List


def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
    ans, diagonal = 0, 0

    for x, y in dimensions:
        aux = x * x + y * y
        area = x * y

        if aux > diagonal:
            diagonal = aux
            ans = area
        elif aux == diagonal:
            ans = max(ans, area)

    return ans


dimensions = [[1, 2], [3, 4], [5, 6]]
print(areaOfMaxDiagonal(None, dimensions))