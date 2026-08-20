# A solução divide os dois primeiros elementos entre arr1 e arr2 e, a partir do terceiro, adiciona cada número ao array cujo último elemento é menor, buscando manter os dois arrays em ordem crescente. Ao final, os dois arrays são concatenados para formar o resultado.

from typing import List

def resultArray(self, nums: List[int]) -> List[int]:
    arr1 = [nums[0]]
    arr2 = [nums[1]]
    for x in range(2, len(nums)):
        if arr1[-1] > arr2[-1]:
            arr1.append(nums[x])
        else:
            arr2.append(nums[x])

    return arr1 + arr2


nums = [1, 2, 3, 4, 5]
print(resultArray(None, nums))
