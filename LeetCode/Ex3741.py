# A função agrupa os índices de cada número do array, depois percorre apenas aqueles que aparecem pelo menos três vezes e, para cada trio consecutivo de ocorrências, calcula uma distância baseada no dobro da diferença entre o primeiro e o terceiro índice, mantendo o menor valor encontrado e retornando -1 caso nenhum número tenha três ocorrências.

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


nums = [1,2,3,4,5]
print(minimumDistance(None, nums))