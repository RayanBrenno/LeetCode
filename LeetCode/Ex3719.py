# Percorre todas as subarrays possíveis usando dois loops, e para cada começo i vai avançando o j contando separadamente os valores ímpares e pares em dois dicionários, e sempre que a quantidade de ímpares distintos fica igual à quantidade de pares distintos, atualiza a resposta com o tamanho da subarray, guardando no final o maior comprimento balanceado encontrado.

from typing import List
def longestBalanced(self, nums: List[int]) -> int:
    ans = 0

    for i in range(len(nums)):
        odd = {}
        even = {}

        for j in range(i, len(nums)):
            if nums[j] & 1:
                odd[nums[j]] = odd.get(nums[j], 0) + 1
            else:
                even[nums[j]] = even.get(nums[j], 0) + 1

            if len(odd) == len(even):
                ans = max(ans, j - i + 1)

    return ans


nums = [1, 2, 3, 4]
print(longestBalanced(None, nums))
