from typing import List


def waysToSplitArray(nums: List[int]) -> int:
    
    res = 0
    r = sum(nums)
    l = 0
    
    for x in range(len(nums)-1):
        print(r, l, nums[x])
        r -= nums[x]
        l += nums[x]
        res += 1 if l > r else 0  
    
    return res


nums = [10,4,-8,7]
print(waysToSplitArray(nums))