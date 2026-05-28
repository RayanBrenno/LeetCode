# O código usa busca binária para encontrar um elemento de pico no array. Ele começa com dois ponteiros (left e right) e, enquanto eles não se encontram, calcula o meio (mid). Se o valor do meio for maior que o próximo elemento, significa que o pico está à esquerda ou no próprio mid, então right = mid. Caso contrário, o pico está à direita, então left = mid + 1. No final, quando left == right, esse índice representa um pico e é retornado.

from typing import List

def findPeakElement(self, nums: List[int]) -> int:
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return left


nums = [1, 2, 3, 1]
print(findPeakElement(None, nums))