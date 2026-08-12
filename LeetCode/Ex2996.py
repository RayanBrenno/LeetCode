# A implementação começa calculando a soma do maior prefixo consecutivo presente no início do array, começando por nums[0] e percorrendo os elementos enquanto cada valor for exatamente o anterior mais 1. Quando a sequência consecutiva é interrompida, o algoritmo para e transforma o array em um set para permitir verificações mais rápidas. Em seguida, enquanto a soma calculada já estiver presente no conjunto, ela é incrementada em 1. Assim, ao final, retornamos o menor inteiro que é maior ou igual à soma do prefixo consecutivo e que não aparece em nums.

from typing import Listw

def missingInteger(self, nums: List[int]) -> int:
    total = nums[0]

    for x in range(1, len(nums)):
        if nums[x-1] + 1 == nums[x]:
            total += nums[x]
        else:
            break

    nums = set(nums)

    while total in nums:
        total += 1

    return total


nums = [1, 2, 3]
print(missingInteger(None, nums))  # Output: 4