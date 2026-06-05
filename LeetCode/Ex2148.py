# Encontra o menor e o maior número da lista e depois conta quantos elementos são estritamente maiores que o menor e estritamente menores que o maior, retornando essa quantidade.

from typing import List

def countElements(self, nums: List[int]) -> int:
    smaller = min(nums)
    greater = max(nums)

    return sum(1 for x in nums if x > smaller and x < greater)


nums = [11, 7, 2, 15]
print(countElements(None, nums))  # Output: 2