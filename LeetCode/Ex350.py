def intersect(nums1, nums2):

    intersect = []
    indexUsed = []
    
    for x in nums1:
        for y in range(len(nums2)):
            if x == nums2[y] and y not in indexUsed:
                intersect.append(x)
                indexUsed.append(y)


    return intersect

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersect(nums1, nums2))