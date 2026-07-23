# A ideia da solução é atribuir um ranking para cada valor distinto do array. Primeiro, são removidos os elementos repetidos com set e os valores restantes são ordenados. Em seguida, é criado um dicionário que associa cada número à sua posição na lista ordenada, começando o ranking em 1. Por fim, percorre-se o array original e substitui-se cada elemento pelo seu respectivo ranking utilizando o dicionário, preservando a ordem original dos elementos e retornando o array transformado.

from typing import List

def arrayRankTransform(self, arr: List[int]) -> List[int]:
    setArr = sorted(set(arr))
    rank = {val: x + 1 for x, val in enumerate(setArr)}
    return [rank[x] for x in arr]


arr = [40, 10, 20, 30]
print(arrayRankTransform(None, arr))  # Output: [4, 1, 2, 3]