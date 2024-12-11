from itertools import permutations

def permute(nums):
    
    return list(permutations(nums))

nums = [1,2,3]
print(permute(nums))