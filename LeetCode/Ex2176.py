def countPairs(nums, k):
    count = 0
    for x in range(len(nums)-1):
        for y in range(x+1, len(nums)):
            if nums[x] == nums[y] and x*y % k == 0:
                count += 1

    return count


nums = [3, 1, 2, 2, 2, 1, 3]
k = 2
print(countPairs(nums, k))
