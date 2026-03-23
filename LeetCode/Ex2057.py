# Esse código percorre a lista nums usando enumerate para ter acesso ao índice (x) e ao valor (y) ao mesmo tempo. Para cada elemento, ele verifica se o índice módulo 10 (x % 10) é igual ao valor armazenado naquela posição. Assim que encontra o primeiro índice que satisfaz essa condição, ele retorna esse índice. Caso nenhum elemento atenda ao critério, a função retorna -1.

from typing import List

def smallestEqual(self, nums: List[int]) -> int:
    for x, y in enumerate(nums):
        if x % 10 == y:
            return x

    return -1


nums = [0,1,2]
print(smallestEqual(None, nums))