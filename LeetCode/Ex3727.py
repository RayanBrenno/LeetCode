# A ideia é elevar todos os elementos ao quadrado e ordenar o array em ordem crescente para separar os valores entre os que serão somados e os que serão subtraídos. Como os maiores valores devem contribuir positivamente para maximizar o resultado, a implementação subtrai a soma da primeira metade dos elementos da soma da segunda metade, retornando a pontuação alternada máxima possível.

from typing import List

def maxAlternatingSum(self, nums: List[int]) -> int:
    n = len(nums)
    for x in range(n):
        nums[x] *= nums[x]
    nums.sort()
    return -sum(nums[: n // 2]) + sum(nums[n // 2:])


nums = [4, 2, 5, 3]
print(maxAlternatingSum(None, nums))