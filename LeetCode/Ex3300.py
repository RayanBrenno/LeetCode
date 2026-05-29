#

from typing import List


def minElement(self, nums: List[int]) -> int:
    ans = float("inf")
    for x in nums:
        aux = 0
        while x:
            aux += x % 10
            x //= 10

        if aux < ans:
            ans = aux

    return ans


    # ans = float("inf")
    # for x in nums:
    #     num = str(x)
    #     aux = sum(int(y) for y in num)
    #     ans = min(ans, aux)
    # return ans
    
    
nums = [16, 23, 5, 42, 8]
print(minElement(None, nums))
