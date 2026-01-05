
from typing import List


def containsNearbyDuplicate(nums: List[int], k: int) -> bool:

    visited = {}
    for index, value in enumerate(nums):
        if value in visited and index - visited[value] <=k:
            return True
        else: 
            visited[value] = index
    return False


nums = [1, 2, 3, 1, 2, 3]
k = 2
print(containsNearbyDuplicate(nums, k))
