from typing import List


def summaryRanges(nums: List[int]) -> List[str]:
    
    res, n = [], len(nums)
    if not nums:
        return res
    start = nums[0]
    for x in range(1, n + 1):
        if x == n or nums[x] != nums[x - 1] + 1:
            if start == nums[x - 1]:
                res.append(str(start))
            else:
                res.append(f"{start}->{nums[x - 1]}")
            if x < n:
                start = nums[x]
    
    return res

nums = [0,1,2,4,5,7]
print(summaryRanges(nums))
    
    
    