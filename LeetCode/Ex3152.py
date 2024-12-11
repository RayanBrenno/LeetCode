def isArraySpecial(nums, queries):
    """
    n = len(nums)
    prefix = [0] * n

    for i in range(1, n):
        prefix[i] = prefix[i - 1]
        if (nums[i - 1] % 2 == 0 and nums[i] % 2 == 0) or (nums[i - 1] % 2 != 0 and nums[i] % 2 != 0):
            prefix[i] += 1

    result = []
    print(prefix)

    for left, right in queries:
        special_count = prefix[right] - (prefix[left] if left > 0 else 0)
        result.append(special_count == 0)

    return result

    """
    n = len(nums)
    
    prefix = [1 if (nums[i - 1] % 2 == nums[i] % 2) else 0 for i in range(1, n)]
    prefix = [0] + prefix  

    res = []

    for start, end in queries:
        has_multiple_ones = sum(prefix[start + 1:end + 1]) > 1
        res.append(not has_multiple_ones)

    return res
    
    """
    def verification(arr):
        aux = 0 if arr[0] % 2 == 0 else 1

        for x in range(1, len(arr)):
            if aux == 0 and arr[x] % 2 == 1:
                aux = 1
                continue
            elif aux == 1 and arr[x] % 2 == 0:
                aux = 0
                continue
            else:
                return False

        return True

    res = []
    for start, end in queries:
        res.append(verification(nums[start:end+1]))

    return res
    """


nums = [4,3,1,6]
queries = [[0,2],[2,3]]
print(isArraySpecial(nums, queries))
