import math
from typing import List
import heapq
import queue


def minOperations(nums: List[int], k: int) -> int:

    heapq.heapify(nums)
    count = 0
    x = heapq.heappop(nums)
    while x < k:
        heapq.heapreplace(nums, x*2 + nums[0])
        x = heapq.heappop(nums)
        count += 1

    return count


nums = [2, 11, 15, 1, 3]
k = 10
print(minOperations(nums, k))
