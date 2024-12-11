def singleNumber(nums):
    res = 0
    for x in nums:
        res ^= x

    return res


nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))
