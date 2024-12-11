from collections import deque


def shortestSubarray(nums, k):
    n = len(nums)
    prefixSum = [0] * (n + 1)

    for i in range(n):
        prefixSum[i + 1] = prefixSum[i] + nums[i]

    dq = deque()
    minLength = float('inf')

    for i in range(n + 1):
        while dq and prefixSum[i] - prefixSum[dq[0]] >= k:
            minLength = min(minLength, i - dq.popleft())

        while dq and prefixSum[i] <= prefixSum[dq[-1]]:
            dq.pop()

        dq.append(i)
        print(dq)
    
    return minLength if minLength != float('inf') else -1


nums = [1, -2,1,-3,-3,6,-5,4,9,-8,-4,-4,5,1,1,6,5,1,1,2,1,3,2,1,5,4,6,4,9,8,6,2,1,2,3,1,7]
k = 4
print(shortestSubarray(nums, k))
