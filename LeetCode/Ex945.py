from typing import List


def minIncrementForUnique(nums: List[int]) -> int:

    nums.sort()
    ans=0
    for x in range(1,len(nums)):
        if nums[x]<=nums[x-1]:
            aux=nums[x-1]-nums[x]+1
            ans+=aux
            nums[x]=nums[x-1]+1
    return ans


nums = [3, 2, 1, 2, 1, 7]
print(minIncrementForUnique(nums))
