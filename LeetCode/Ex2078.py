# A função percorre o array duas vezes para encontrar a maior distância entre casas com cores diferentes: primeiro ela compara todas as casas a partir do final com a primeira casa, parando na primeira que tiver cor diferente e guardando essa distância (num1), depois faz o contrário, percorrendo do início e comparando com a última casa para encontrar outra distância válida (num2); como a maior distância possível sempre envolve uma das extremidades do array, ela retorna o máximo entre esses dois valores.

from typing import List

def maxDistance(self, colors: List[int]) -> int:
    n = len(colors)
    num1, num2 = 0, 0
    for x in range(n-1, -1, -1):
        if colors[x] != colors[0]:
            num1 = x
            break

    for x in range(n):
        if colors[x] != colors[-1]:
            num2 = n - x - 1
            break

    return max(num1, num2)


colors = [1, 1, 1, 6, 1, 1, 1]
print(maxDistance(None, colors))