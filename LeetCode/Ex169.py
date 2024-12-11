def majorityElement(nums):

    visit = set()
    n = len(nums) - 1
    for x in nums:
        if x not in visit:
            visit.add(x)
            if nums.count(x) > n//2:
                return x
        else:
            continue
        
nums = [3,2,3]
print(majorityElement(nums))
