def nthUglyNumber(n):
    nums = [0] * n
    count1 = count2 = count3 = 0
    nums[0] = 1
    for i in range(1, n):
        nums[i] = min(nums[count1]*2, nums[count2]*3, nums[count3]*5)
        if (nums[i] == nums[count1]*2): count1 += 1
        if (nums[i] == nums[count2]*3): count2 += 1
        if (nums[i] == nums[count3]*5): count3 += 1
        
    return nums[n-1]


n = 10
print(nthUglyNumber(n))
