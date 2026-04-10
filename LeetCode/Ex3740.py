# A função agrupa os índices de cada número do array usando um dicionário, onde cada valor aponta para uma lista com todas as posições em que aparece. Em seguida, percorre esses grupos e, para aqueles que têm pelo menos três ocorrências, analisa trios consecutivos de índices. Para cada trio, calcula a distância mínima possível usando a fórmula otimizada 2 * (k - i), considerando apenas o primeiro e o último índice do trio. Durante o processo, mantém o menor valor encontrado e, ao final, retorna essa menor distância ou -1 caso não exista nenhum trio válido.

from collections import defaultdict
from typing import List

def minimumDistance(self, nums: List[int]) -> int:
    count = defaultdict(list)

    for index, num in enumerate(nums):
        count[num].append(index)

    ans = float('inf')

    for rep in count.values():
        if len(rep) >= 3:
            for x in range(len(rep) - 2):
                dist = 2 * (rep[x+2] - rep[x])
                ans = min(ans, dist)

    return ans if ans != float('inf') else -1


nums = [1, 2, 3, 1, 2, 3, 1]
print(minimumDistance(nums)) 