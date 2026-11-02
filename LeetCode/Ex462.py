# A ideia é ordenar o array e escolher a mediana como valor de referência, pois ela minimiza a quantidade total de movimentos necessários para igualar todos os elementos. Em seguida, percorremos o array somando a diferença absoluta entre cada número e a mediana, calculando assim o total de movimentos necessários para tornar todos os valores iguais.

from typing import List


def minMoves2(self, nums: list[int]) -> int:
    nums.sort()
    aux = nums[len(nums) // 2]
    ans = 0
    for x in nums:
        ans += abs(x - aux)
    return ans


nums = [1, 2, 3]
print(minMoves2(None, nums))
