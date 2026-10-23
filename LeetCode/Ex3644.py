# A ideia é percorrer o vetor e verificar quais elementos estão fora de suas posições corretas, ou seja, quando nums[x] != x. Para esses elementos, fazemos o AND bit a bit (&) entre seus valores, armazenando o resultado em ans. Como ans começa em -1, todos os bits começam ligados, permitindo que o AND seja aplicado aos elementos encontrados. No final, retornamos ans, ou 0 caso todos os elementos já estejam nas posições corretas.

from typing import List


def sortPermutation(self, nums: List[int]) -> int:
    n = len(nums)
    ans = -1

    for x in range(n):
        if nums[x] == x:
            continue
        ans &= nums[x]

    return ans if ans != -1 else 0


nums = [2, 0, 1, 3]
result = sortPermutation(nums)
