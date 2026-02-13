from collections import Counter
from typing import List


def findDuplicate(self, nums: List[int]) -> int:

    n = len(nums)
    aux = [False] * (n)
    for x in nums:
        if aux[x]:
            return x
        else:
            aux[x] = True

    # counter = Counter(nums)
    # for x, y in counter.items():
    #     if y > 1:
    #         return x


nums = [1, 3, 4, 2, 2]
print(findDuplicate(None, nums))
