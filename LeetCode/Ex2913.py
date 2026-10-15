# A implementação percorre todos os subarrays possíveis de nums, utilizando um set para armazenar os elementos distintos de cada subarray. A cada novo elemento adicionado ao conjunto, soma ao resultado o quadrado da quantidade de elementos distintos encontrados. Ao final, retorna ans com a soma dos quadrados de todos os subarrays.

from typing import List


def sumCounts(self, nums: List[int]) -> int:
    n = len(nums)
    ans = 0
    for x in range(n):
        aux = set()
        for y in range(x, n):
            aux.add(nums[y])
            ans += len(aux)**2
    return ans


nums = [1, 2, 3]
print(sumCounts(None, nums))