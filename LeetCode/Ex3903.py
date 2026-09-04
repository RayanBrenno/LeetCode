# A implementação percorre os índices do array e, para cada posição, calcula o maior valor desde o início até i e o menor valor de i até o final. Se a diferença entre esses dois valores for menor ou igual a k, o índice é estável e é retornado imediatamente. Caso nenhum índice satisfaça a condição, retorna -1.

from typing import List

def firstStableIndex(self, nums: List[int], k: int) -> int:
    for i in range(len(nums)):
        if max(nums[:i + 1]) - min(nums[i:]) <= k:
            return i

    return -1


nums = [1, 3, 6, 4, 1]