# A ideia é igualar todos os elementos ao maior valor do array, considerando que cada movimento aumenta um elemento em 1. Para isso, multiplicamos o maior valor pelo tamanho do array e subtraímos a soma dos elementos, obtendo diretamente a quantidade mínima de movimentos necessários.

from typing import List


def minMoves(self, nums: List[int]) -> int:

    return max(nums) * len(nums) - sum(nums)

    # nums.sort()
    # ans = 0
    # for x in nums:
    #     ans += abs(x - nums[-1])
    # return ans


nums = [1, 2, 3]
print(minMoves(None, nums))
