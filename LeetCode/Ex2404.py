from collections import defaultdict


def mostFrequentEven(nums):
    nums = [x for x in nums if x % 2 == 0]
    if len(nums) == 0:
        return -1
    nums.sort()
    res = defaultdict(int)
    for x in nums:
        res[x] += 1

    res = sorted(res.items(), key=lambda item: item[1], reverse=True)
    return res[0][0]


nums = [8154, 9139, 8194, 3346, 5450, 9190, 133, 8239, 4606, 8671, 8412, 6290]
print(mostFrequentEven(nums))
