import heapq
import math
from typing import List


def pickGifts(gifts: List[int], k: int) -> int:

    heap = [-x for x in gifts]
    heapq.heapify(heap)
    while k > 0:
        heapq.heapreplace(heap,-math.isqrt(-heap[0]))
        k -= 1

    return -sum(heap)


gifts = [25, 64, 9, 4, 100,]
k = 4
print(pickGifts(gifts, k))
