# A função percorre a lista uma única vez mantendo um dicionário que mapeia cada número invertido para o índice onde ele apareceu anteriormente. Para cada elemento atual, ela verifica se esse número já existe como chave no dicionário, o que significa que algum número anterior tem como reverso o valor atual; quando isso acontece, calcula a distância entre os índices e mantém a menor encontrada. Em seguida, armazena no dicionário o reverso do número atual apontando para seu índice, permitindo que ele seja usado em comparações futuras. Ao final, retorna a menor distância encontrada ou -1 caso nenhum par válido exista.

from typing import List


def minMirrorPairDistance(self, nums: List[int]) -> int:
    reverse = {}
    ans = float("inf")
    for index, num in enumerate(nums):
        if num in reverse:
            ans = min(ans, abs(reverse[num] - index))
        reverse[int(str(num)[::-1])] = index

    return ans if ans != float('inf') else -1


nums = [123, 321, 456, 654]
print(minMirrorPairDistance(None, nums))
