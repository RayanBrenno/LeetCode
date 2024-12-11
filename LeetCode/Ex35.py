def searchInsert(nums, target):

    for x in range(len(nums)):
        if nums[x] == target:
            return x

        elif nums[x] > target:
            return x
        
        elif nums[x] < target and x == len(nums)-1:
            return x+1


nums = [1, 3, 5, 6, 7, 8, 10]
target = 11
print(searchInsert(nums, target))
