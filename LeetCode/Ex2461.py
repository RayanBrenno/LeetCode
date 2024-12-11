from collections import defaultdict

def maximumSubarraySum(nums, k):
    res = 0
    count = defaultdict(int)
    currentSum = 0

    left = 0
    for right in range(len(nums)):
        currentSum += nums[right]
        count[nums[right]] += 1
        if right - left + 1 > k:
            count[nums[left]] -= 1
            if count[nums[left]] == 0:
                count.pop(nums[left])
            currentSum -= nums[left]
            left += 1

        if len(count) == right - left + 1 == k:
            res = max(res, currentSum)

    return res
    """
    n = len(nums) - k + 1
    nums = nums+nums

    res = 0
    for x in range(n):
        arr = nums[x:x+k]
        if len(set(arr)) == k:
            res = max(res, sum(arr))

    return res
    """


nums = [1,5,4,2,9,9,9]
k = 3
print(maximumSubarraySum(nums, k))
