def countKDifference(nums, k):
    count = 0
    for x in range(len(nums)-1):
        for y in range(x, len(nums)):
            if abs(nums[x]-nums[y]) == k:
                count += 1

    return count


nums = [1, 2, 2, 1]
k = 1
print(countKDifference(nums, k))
