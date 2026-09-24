# A implementação percorre o array junto com seus índices, calcula a soma dos dígitos de cada número usando um `while` e, quando essa soma é igual ao índice atual, retorna esse índice. Caso nenhum número satisfaça a condição, retorna `-1`.

from typing import List


def smallestIndex(self, nums: List[int]) -> int:
    for index, num in enumerate(nums):
        aux = 0
        while num > 0:
            aux += num % 10
            num //= 10
        if aux == index:
            return index
    return -1


nums = [18, 29, 38, 49, 50]
print(smallestIndex(nums))  # Saída: 1
