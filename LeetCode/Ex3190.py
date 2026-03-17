from typing import List

def minimumOperations(self, nums: List[int]) -> int:
    arr = [min(x % 3, 3 - (x % 3)) for x in nums]
    return sum(arr)


nums = [1, 2, 3, 4, 5]
print(minimumOperations(None, nums))