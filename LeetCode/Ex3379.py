from typing import List
def constructTransformedArray(self, nums: List[int]) -> List[int]:
    n = len(nums)
    ans = []
    for i in range(n):
        ans.append(nums[((i + nums[i]) % n + n) % n])
    return ans

# Example usage:
print(constructTransformedArray(None, [3,-2,1,1]))  # Output: [7, 11, 7, 11]