from typing import List

def minStartValue(self, nums: List[int]) -> int:
    prefix_sum = 0
    aux = 0

    for x in nums:
        prefix_sum += x
        aux = min(aux, prefix_sum)

    return 1 - aux


nums = [-3, 2, -3, 4, 2]
print(minStartValue(nums))