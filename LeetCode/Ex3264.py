import heapq
from typing import List


def getFinalState(nums: List[int], k: int, multiplier: int) -> List[int]:

    for _ in range(k):
        index = nums.index(min(nums))
        nums[index] *= multiplier

    return nums


nums = [2, 1, 3, 5, 6]
k = 5
multiplier = 2
print(getFinalState(nums, k, multiplier))
