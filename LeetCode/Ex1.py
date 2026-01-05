def twoSum(nums, target):
    output = []
    for x in nums:
        for y in range(nums.index(x)+1,len(nums)):
            if(x+nums[y] == target):
                output = [nums.index(x), y]
                return output

    return output

print(twoSum([2,7,11,15],9))

    