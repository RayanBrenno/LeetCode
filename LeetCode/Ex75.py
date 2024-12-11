def sortColors(nums):
    trade = False
    for x in range(len(nums)):
        for y in range(x+1, len(nums)):
            if nums[x] > nums[y]:
                nums[x], nums[y] = nums[y], nums[x]
                trade = True
        
        if not trade:
            break

    return nums


nums = [0, 2, 1]
print(sortColors(nums))
