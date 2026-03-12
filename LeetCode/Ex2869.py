# A ideia é descobrir quantas operações são necessárias olhando o array de trás para frente até encontrar todos os números de 1 até k. Primeiro criamos uma lista collection com os números de 1 até k. Depois percorremos nums do final para o início. Cada vez que encontramos um número que está em collection, removemos ele. Quando collection fica vazia, significa que já encontramos todos os números necessários, então retornamos n - x, que representa quantos elementos do final precisaram ser verificados (ou removidos) para coletar todos os números de 1 até k.

from typing import List

def minOperations(self, nums: List[int], k: int) -> int:
    collection = [x for x in range(1, k+1)]
    n = len(nums)
    for x in range(n-1, -1, -1):
        aux = nums[x]
        if aux in collection:
            collection.remove(aux)
        if len(collection) == 0:
            return n - x


nums = [3, 2, 1, 5, 4]
k = 2
print(minOperations(None, nums, k))