def searchRange(nums, target):
    aux = 0
    output = [-1, -1]
    if target not in nums:
        return output
    else:
        while True:
            if nums[aux] == target:
                output[0] = aux
                while aux < len(nums):
                    if nums[aux] != target:
                        break
                    aux+=1
                output[1] = aux -1
                break
            aux += 1
        return output
    
nums = [5,7,7,8,8,8]
target = 8
print(searchRange(nums, target))