import heapq
from git import List


def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
    happiness.sort(reverse=True)
    ans = 0
    for x in range(k):
        aux = happiness[x] - x
        if aux < 0:
            break
        ans += aux
    return ans
    
    # heap = [-x for x in happiness]
    # heapq.heapify(heap)
    
    # ans = 0
    # count = 0
    
    # for _ in range(k):
    #     if not heap:
    #         break
    #     ans += max(-heapq.heappop(heap) - count, 0)
    #     count += 1
    
    
    # return ans


happiness = [1, 2, 3]
k = 2
print(maximumHappinessSum(None, happiness, k))