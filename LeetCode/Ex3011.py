def canSortArray(nums):
    def countBit(binarie):
        count = 0
        for x in binarie:
            if x == '1':
                count+=1
        return count

    for x in range(len(nums)-1):
        for y in range(len(nums)-1):
            if nums[y]>nums[y+1] and countBit(bin(nums[y])) == countBit(bin(nums[y+1])):
                nums[y], nums[y + 1] = nums[y + 1], nums[y]
        
    return True if nums == sorted(nums) else False

nums = [3,16,8,4,2]
print(canSortArray(nums))

string = 'sasasasaa'
print(string.count('sa'))