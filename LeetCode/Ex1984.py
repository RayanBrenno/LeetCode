
from typing import List


def minimumDifference(self, nums: List[int], k: int) -> int:
    # nums.sort()
    # n = len(nums)
    # ans = float('inf')
    # for x in range(n - k + 1):
    #     aux = nums[x:x + k]
    #     ans = min(ans, aux[-1] - aux[0])

    # return ans if ans != float('inf') else 0
    
    if k == 1:
        return 0
    nums.sort()
    n = len(nums)

    return min(nums[i + k - 1] - nums[i] for i in range(n - k + 1))


nums = [87063, 61094, 44530, 21297, 95857, 93551, 9918]
k = 6
print(minimumDifference(None, nums, k))  # Example usage
