# O código verifica se o elemento do meio da lista aparece exatamente uma vez em nums, utilizando count() para contar suas ocorrências e retornando True caso seja único ou False caso contrário.

from typing import List


def isMiddleElementUnique(self, nums: List[int]) -> bool:
    return True if nums.count(nums[len(nums)//2]) == 1 else False


nums = [1, 2, 3, 4, 5]
print(isMiddleElementUnique(None, nums))
