def containsDuplicate(nums):
    return False if len(nums) == len(set(nums)) else True 


nums = [1,2,3,1]
print(containsDuplicate(nums))