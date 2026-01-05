import math
from typing import List
import heapq

def minStoneSum(piles: List[int], k: int) -> int:
    
    nums = [-x for x in piles]
    heapq.heapify(nums)
    for _ in range(k):
        heapq.heapreplace(nums, math.floor(nums[0]/2))   
    return -sum(nums)

piles = [5,4,9]
k = 2
print(minStoneSum(piles, k))