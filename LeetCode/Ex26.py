def removeDuplicates(nums):
    uniqueNum = []
    nums.sort()

    for x in range(len(nums)-1,-1,-1):
        if nums[x] not in uniqueNum: uniqueNum.append(nums[x])
        else: nums.pop(x)


    return len(nums)

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))
