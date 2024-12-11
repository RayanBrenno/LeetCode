def maxNumOfMarkedIndices(nums):
    nums.sort()
    i = 0
    print(nums)
    for j in range((len(nums) + 1) // 2, len(nums)):
        if nums[i] * 2 <= nums[j]:
            print(nums[i] * 2, nums[j])
            i += 1
    return 2 * i


nums = [1, 3, 5, 7, 10, 9, 80, 161]
print(maxNumOfMarkedIndices(nums))
