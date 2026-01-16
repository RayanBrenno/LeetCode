# Esse exercício é direto: a ideia é somar todos os valores do array e verificar o resto dessa soma ao dividir por k. Esse resto representa exatamente quantas operações ainda são necessárias para que a soma total se torne múltipla de k.

from typing import List

def minOperations(self, nums: List[int], k: int) -> int:
    return sum(nums) % k

print(minOperations(None, [1, 2, 3, 4, 5], 3))
print(minOperations(None, [5, 10, 2], 5))