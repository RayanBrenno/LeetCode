from typing import List
import heapq

def minimumCost(self, nums: List[int]) -> int:
    if len(nums) == 3:
        return sum(nums)
    ans = nums[0]
    nums.pop(0)
    heapq.heapify(nums)
    
    ans += heapq.heappop(nums)
    ans += heapq.heappop(nums)
    
    return ans



nums = [4, 2, 3, 6, 5]
print(minimumCost(None, nums))  # Example usage