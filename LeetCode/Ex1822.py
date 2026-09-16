# A implementação percorre todos os elementos do array contando quantos números negativos existem. Se encontrar algum 0, retorna 0 imediatamente, pois o produto será zero. No final, verifica a paridade da quantidade de negativos: se for ímpar, o produto é negativo e retorna -1; caso seja par, o produto é positivo e retorna 1.

from typing import List


def arraySign(self, nums: List[int]) -> int:
    countNeg = 0
    for x in nums:
        if x == 0:
            return 0
        countNeg += 1 if x < 0 else 0
    return -1 if countNeg % 2 != 0 else 1


nums = [-1, -2, -3, -4, 3, 2, 1]
print(arraySign(nums))  # Saída: 1
