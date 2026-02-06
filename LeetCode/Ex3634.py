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