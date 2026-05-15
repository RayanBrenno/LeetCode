# A função encontra o menor número em um array que foi rotacionado. Ela usa busca binária comparando o elemento do meio com o da direita. Se o meio é maior que a direita, o número menor está na metade direita, então descarta a esquerda. Se o meio é menor ou igual, descarta a direita. Continua cortando pela metade até achar o ponto onde a rotação quebrou a ordem e encontra o mínimo lá.

from typing import List


def findMin(self, nums: List[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]

    # return min(nums)


nums = [3, 4, 5, 1, 2]
print(findMin(nums))  # Output: 1