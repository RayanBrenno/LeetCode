# A função encontra o menor número em um array rotacionado que pode ter elementos repetidos. Usa busca binária comparando o elemento do meio com o da direita. Se o meio é maior, o mínimo está à direita e descarta a esquerda. Se o meio é menor, descarta a direita. Quando o meio é igual à direita (duplicata), não dá pra saber de qual lado está o mínimo, então só encolhe a direita de um em um. Continua até achar o ponto onde a rotação quebrou a ordem e encontra o mínimo.


from typing import List


def findMin(self, nums: List[int]) -> int:
    left, right = 0, len(nums) - 1

    while left != right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        elif nums[mid] < nums[right]:
            right = mid
        else:
            right -= 1

    return nums[left]


nums = [3, 4, 5, 1, 2]
print(findMin(nums))  # Output: 1
nums = [3, 3, 1, 3]
print(findMin(nums))  # Output: 1
