def findLengthOfShortestSubarray(arr):
    n = len(arr)

    left = 0
    while left < n - 1 and arr[left] <= arr[left + 1]:
        left += 1

    right = n - 1
    while right > 0 and arr[right - 1] <= arr[right]:
        right -= 1

    if left >= right:
        return 0

    res = min(n-left-1, right)

    l = 0

    while l <= left and right < n:
        if arr[l] <= arr[right]:
            res = min(res, right-l-1)
            l += 1
        else:
            right += 1
    return res


arr = [1, 2, 3, 10, 4, 2, 3, 5]

print(findLengthOfShortestSubarray(arr))
