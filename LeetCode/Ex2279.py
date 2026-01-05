from typing import List
import heapq


def maximumBags(capacity: List[int], rocks: List[int], additionalRocks: int) -> int:

    diff = sorted(capacity-rocks for capacity, rocks in zip(capacity, rocks))
    res = 0
    for x in diff:
        if additionalRocks >= x:
            additionalRocks -= x
            res += 1
        else:
            return res
    return res

    """
    res = 0
    heap = []
    for capacity, rocks in zip(capacity, rocks):
        if capacity == rocks: 
            res+=1
            continue
        heap.append(capacity-rocks)
    
    heapq.heapify(heap)
    while additionalRocks > 0:
        if len(heap) == 0: break
        aux = heapq.heappop(heap)
        res += 1 if additionalRocks-aux >= 0 else 0
        additionalRocks -=aux

    return res
    """


capacity = [2, 3, 4, 5]
rocks = [1, 2, 4, 4]
additionalRocks = 2
print(maximumBags(capacity, rocks, additionalRocks))
