# O código conta quantos pares iguais existem no array. Primeiro, o Counter armazena quantas vezes cada número aparece. Depois, para cada frequência x, ele calcula quantos pares podem ser formados usando a fórmula (x * (x - 1)) // 2, somando tudo em ans. No final, retorna a quantidade total de pares idênticos.

from collections import Counter
from typing import List

def numIdenticalPairs(self, nums: List[int]) -> int:
    count = Counter(nums)
    ans = 0
    for x in count.values():
        ans += (x*(x-1))//2

    return ans


nums = [1, 2, 3, 1, 1, 3]
print(numIdenticalPairs(None, nums))