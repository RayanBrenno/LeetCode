from typing import List

def countPartitions(self, nums: List[int]) -> int:
    total_sum = sum(nums)
    count = 0
    left_sum = 0
    for i in range(len(nums) - 1):
        left_sum += nums[i]
        right_sum = total_sum - left_sum

        if (left_sum % 2) == (right_sum % 2):
            count += 1

    return count

# Conta o número de maneiras de particionar uma lista em dois subarrays com soma par.
nums = [10,10,3,7,6]
print(countPartitions(None, nums))
