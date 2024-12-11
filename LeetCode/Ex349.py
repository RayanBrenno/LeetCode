def intersection(nums1, nums2):

    nums1 = set(nums1)
    nums2 = set(nums2)
    intersection = list(nums1.intersection(nums2))
    return intersection


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersection(nums1, nums2))
