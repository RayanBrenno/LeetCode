# Como é permitido escolher o mesmo subarray quantas vezes quiser, a melhor estratégia é encontrar o subarray de maior valor possível. Esse valor é obtido pela diferença entre o maior e o menor elemento do array, e então basta multiplicá-lo por k, escolhendo esse mesmo subarray k vezes.

from typing import List

def maxTotalValue(self, nums: List[int], k: int) -> int:
    aux1 = min(nums)
    aux2 = max(nums)
    return (aux2 - aux1) * k


nums = [1, 2, 3, 4, 5]
k = 2
print(maxTotalValue(None, nums, k))  # Output: 8