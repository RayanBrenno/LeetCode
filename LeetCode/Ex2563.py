def countFairPairs(nums, lower, upper):
    
    nums.sort()
    count = 0
    left = right = len(nums) - 1
    
    for x in range(len(nums) - 1):

        while right > x and nums[x] + nums[right] > upper:
            right -= 1

        while left > x and nums[x] + nums[left] >= lower:
            left -= 1

        if right > x:
            count += right - max(left, x)

    return count

    """
    count = 0
    n = len(nums)
    nums.sort()
    for i in range(n):
        for j in range(i, n):
            if 0 <= i < j < n and lower <= nums[i] + nums[j] <= upper:
                count += 1

    return count
    """


nums = [0, 1, 7, 4, 4, 5]
lower = 3
upper = 6
print(countFairPairs(nums, lower, upper))
