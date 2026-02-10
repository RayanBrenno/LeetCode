# Ordena o array pra facilitar a comparação, usa dois ponteiros onde o r percorre os elementos e o l marca o menor válido, sempre que nums[r] fica maior que nums[l] * k significa que esse menor não serve mais então l anda, e no final o valor de l representa a quantidade mínima de elementos que precisam ser removidos.

from typing import List

def minRemoval(self, nums: List[int], k: int) -> int:
    nums.sort()
    l = 0

    for r in range(len(nums)):
        if nums[r] > nums[l] * k:
            l += 1
    return l

nums = [1, 2, 3, 4, 5]
k = 2
print(minRemoval(None, nums, k))