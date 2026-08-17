# A implementação usa XOR para verificar se é possível manter toda a sequência. Primeiro, percorre nums, calculando o XOR acumulado e verificando se existe pelo menos um elemento diferente de zero. Se o XOR final for maior que zero, significa que toda a sequência pode ser mantida, então retorna n. Caso o XOR seja zero, é necessário remover um elemento; se existir algum elemento diferente de zero, retorna n - 1, enquanto uma sequência composta apenas por zeros retorna 0.

from typing import List

def longestSubsequence(self, nums: List[int]) -> int:
    xor = 0
    aux = False

    for x in nums:
        xor ^= x
        if x != 0:
            aux = True

    n = len(nums)
    if xor > 0:
        return n

    return n - 1 if aux else 0


nums = [1, 2, 3, 0, 4]
print(longestSubsequence(None, nums))