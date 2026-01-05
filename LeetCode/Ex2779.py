def maximumBeauty(nums, k):
    nums.sort()
    res, left = 0, 0
    for right in range(len(nums)):
        while nums[right] - nums[left] > 2 * k:
            left += 1
        res = max(res, right-left+1)
    return res


nums = [4,6,1,2]
k = 2
print(maximumBeauty(nums, k))
