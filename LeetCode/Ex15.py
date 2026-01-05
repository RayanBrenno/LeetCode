def threeSum(nums):
    output = []
    nums.sort()
    for x in range(len(nums)):
        y = x + 1
        z = len(nums) - 1
        while y < z:
            value = nums[x] + nums[y] + nums[z]
            auxArr = sorted([nums[x], nums[y], nums[z]])
            if value == 0:
                if auxArr not in output: output.append(auxArr)
                y += 1
            elif value < 0:
                y += 1
            else:
                z -= 1

    return output

    """
    output = []
    for x in range(len(nums) - 2):
        for y in range(x + 1, len(nums) - 1):
            for z in range(y + 1, len(nums)):
                if nums[x] + nums[y] + nums[z] == 0:
                    aux = [nums[x], nums[y], nums[z]]
                    if aux not in output:
                        output.append(aux)
    
    return sorted(output)
    """


nums = [-2, 0, 1, 1, 2]
print(threeSum(nums))
