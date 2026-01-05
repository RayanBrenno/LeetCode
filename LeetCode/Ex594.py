from typing import Counter, List


def findLHS(nums: List[int]) -> int:

    counter = Counter(nums)
    res = 0 
    for x in counter.keys():
        if x - 1 in counter:
            res = max(counter[x] + counter[x-1], res)
    return res

    """
    nums.sort()
    i, j = 0, 0
    n, res = len(nums), 0
    while j < n:
        while nums[j]-nums[i] > 1:
            i += 1
        if nums[j]-nums[i] == 1:
            res = max(res, j-i+1)
        j += 1
    return res
    """


nums = [1, 3, 2, 2, 5, 2, 3, 7]
print(findLHS(nums))
