def largestSumAfterKNegations(nums, k):
    res = sum(nums)
    while k > 0:
        minValue = min(nums)
            
        k -= 1
        nums[nums.index(minValue)] = minValue * -1
    return res


nums = [3,-1,0,2]
k = 3
print(largestSumAfterKNegations(nums, k))
