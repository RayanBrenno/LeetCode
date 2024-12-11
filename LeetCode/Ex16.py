def threeSumClosest(nums, target):
    nums.sort()
    closestSum = float('inf')
    for x in range(len(nums)-2):
        left, right = x + 1, len(nums) - 1
        while left != right:
            sumValue = nums[x] + nums[left] + nums[right]
            
            if abs(sumValue - target) < abs(closestSum - target): closestSum = sumValue
                
            if sumValue < target: left += 1      
            elif sumValue > target: right -= 1
            else: return sumValue
    
    return closestSum


nums = [1, 2, 1, -5]
target = 1
print(threeSumClosest(nums, target))
