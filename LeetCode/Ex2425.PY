from typing import List


def xorAllNums(nums1: List[int], nums2: List[int]) -> int:

    res = 0
    if len(nums1) % 2 == 1:
        for x in nums2:
            res = res ^ x

    if len(nums2) % 2 == 1:
        for x in nums1:
            res = res ^ x

    return res


nums1 = [1]
nums2 = [3, 4]
print(xorAllNums(nums1, nums2))
