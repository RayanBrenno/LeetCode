# Ordeno o array para facilitar a identificação dos menores e maiores elementos e, em seguida, calculo as três possibilidades de diferença que permanecem após alterar dois elementos: removendo os dois menores, o menor e o maior ou os dois maiores. Como podemos fazer com que os dois elementos alterados tenham o mesmo valor, o low será sempre zero, então basta retornar a menor diferença encontrada entre as três possibilidades.

from typing import List


def minimizeSum(self, nums: List[int]) -> int:
    nums.sort()

    n = len(nums)

    return min(
        nums[n-1] - nums[2],
        nums[n-2] - nums[1],
        nums[n-3] - nums[0]
    )


nums = [1, 4, 7, 8, 5]
print(minimizeSum(None, nums))
