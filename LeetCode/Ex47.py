from itertools import permutations

def permuteUnique(nums):
    permuta = list(permutations(nums))
    unique=[]
    
    for x in range(len(permuta)-1, -1, -1):
        if permuta[x] not in unique: unique.append(permuta[x])
        else: permuta.pop(x)
        
    return permuta

nums = [1,1,2]
print(permuteUnique(nums))