def findMedianSortedArrays(nums1, nums2):
        nums = nums1 + nums2 
        nums.sort()
        value = nums[len(nums)//2] if len(nums)%2 == 1 else (nums[len(nums)//2-1] + nums[len(nums)//2] ) / 2
        return value
    
nums1 = [1,2]
nums2 = [3,4]
print(findMedianSortedArrays(nums1, nums2))



