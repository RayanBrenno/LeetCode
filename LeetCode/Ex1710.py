from typing import List
import heapq
def maximumUnits(boxTypes: List[List[int]], truckSize: int) -> int:
    
    heap = [(-unit, box) for box, unit in boxTypes]
    heapq.  (heap)
    res = 0
    while truckSize > 0:
        print(heap)
        if len(heap) == 0: break
        units, boxs = heapq.heappop(heap)
        if truckSize - boxs > 0:
            res += boxs*(-units)
            truckSize -=boxs
        else: 
            res += truckSize*(-units)
            truckSize = -1
    return res



boxTypes = [[1,3],[5,5],[2,5],[4,2],[4,1],[3,1],[2,2],[1,3],[2,5],[3,2]]
truckSize = 35
print(maximumUnits(boxTypes, truckSize))