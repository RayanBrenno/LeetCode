import math

def majorityElement(nums):

    res = []
    visit = set()
    n = len(nums)
    minPer = math.ceil((1 / 3) * 100)
    for x in nums:
        if x not in visit:
            numPer = math.ceil((nums.count(x)/n) * 100)
            visit.add(x)
            if numPer > minPer:
                res.append(x)

    return res


nums = [3, 2, 3]
print(majorityElement(nums))
