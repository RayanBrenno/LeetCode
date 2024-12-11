def resultsArray(nums, k):

    if k == 1:
        return nums
    n = len(nums)
    res = [0] * (n-k+1)

    for x in range(n-k+1):
        arr = nums[x:x+k]
        aux = 0
        bol = True
        while aux < len(arr)-1:
            if arr[aux+1] != arr[aux] + 1:
                bol = False
                break
            aux += 1

        res[x] = arr[-1] if bol else -1

    return res


nums = [1, 3, 4]
k = 2
print(resultsArray(nums, k))
