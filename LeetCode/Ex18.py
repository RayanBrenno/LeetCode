def fourSum(nums, target):
    output = []
    nums.sort()

    for x in range(len(nums)-3):
        for y in range(x+1, len(nums)-2):
            midLeft, midRight = y+1, len(nums)-1
            while midLeft < midRight:
                sumValue = nums[x] + nums[y] + nums[midRight] + nums[midLeft]

                if sumValue < target:
                    midLeft += 1
                elif sumValue > target:
                    midRight -= 1
                else:
                    aux = [nums[x], nums[y], nums[midLeft], nums[midRight]]
                    if sorted(aux) not in output:
                        output.append(sorted(aux))
                    midLeft += 1
                    midRight -= 1

    return output


nums = [1, 0, -1, 0, -2, 2]
target = 0
print(fourSum(nums, target))
