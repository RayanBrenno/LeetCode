# A implementação conta quantos números pares existem no array usando uma expressão geradora e `sum()`. Como o OR bit a bit de dois números é par quando ambos são pares, basta verificar se existem pelo menos dois números pares. Se a contagem for maior ou igual a 2, retorna `True`; caso contrário, `False`.

from typing import List


def hasTrailingZeros(self, nums: List[int]) -> bool:
    # n = len(nums)

    # for x in range(n):
    #     for y in range(x + 1, n):
    #         if x != y and (nums[x] | nums[y]) % 2 == 0:
    #             return True
    # return False

    return sum(1 for x in nums if x % 2 == 0) >= 2


nums = [1, 3, 5, 7, 9]
print(hasTrailingZeros(nums))  # Saída: False
