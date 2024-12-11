def merge(nums1, m, nums2, n):

    num1 = m - 1  
    num2 = n - 1  

    for x in range(n + m - 1, -1, -1):
        if num2 < 0:
            break  

        if num1 >= 0 and nums1[num1] > nums2[num2]:
            nums1[x] = nums1[num1]
            num1 -= 1  
        else:
            nums1[x] = nums2[num2]
            num2 -= 1  
    
    return nums1

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
print(merge(nums1, m, nums2, n))
