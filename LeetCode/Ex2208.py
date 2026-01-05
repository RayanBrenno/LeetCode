import math
from typing import List
import heapq
import queue


def halveArray(nums: List[int]) -> int:
    heap = [-x for x in nums]
    heapq.heapify(heap)
    half, count = sum(heap)/2, 0
    while half < 0:
        aux = heapq.heappop(heap)
        aux /= 2 
        half -= aux
        heapq.heappush(heap,aux)
        count += 1
        
    return count

    """
    heap = [-x for x in nums]
    heapq.heapify(heap)
    count = 0
    while -sum(heap) > sum(nums)/2:
        heapq.heapreplace(heap, heap[0]/2)
        count += 1
    return count
    """


nums = [5, 19, 8, 1]
print(halveArray(nums))
