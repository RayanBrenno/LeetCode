# O algoritmo encontra as posições do menor e do maior elemento do array e organiza esses índices como left e right. A partir disso, calcula as três formas possíveis de removê-los: removendo tudo pela esquerda até o elemento mais à direita, removendo tudo pela direita até o elemento mais à esquerda ou removendo um elemento por cada extremidade, e então retorna a menor quantidade de deleções entre essas três opções.

from typing import List


def minimumDeletions(self, nums: List[int]) -> int:
    n = len(nums)

    minIndex = nums.index(min(nums))
    maxIndex = nums.index(max(nums))

    left = min(minIndex, maxIndex)
    right = max(minIndex, maxIndex)

    return min(right + 1, n - left, left + 1 + (n - right))


nums = [2, 10, 7, 5, 4, 1, 8, 6]
print(minimumDeletions(None, nums))  # Output: 5
