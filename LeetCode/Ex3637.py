# A ideia é percorrer o array verificando se ele segue exatamente três fases consecutivas: primeiro um trecho estritamente crescente, depois um trecho estritamente decrescente e, por fim, outro trecho estritamente crescente. O índice avança enquanto cada condição é satisfeita e, se alguma fase não existir ou terminar antes do esperado, o array é considerado inválido. No final, só retorna verdadeiro se todos os elementos forem consumidos respeitando essa sequência.

from typing import List


def isTrionic(self, nums: List[int]) -> bool:
    n = len(nums)
    if n < 3:
        return False

    i = 0

    while i + 1 < n and nums[i] < nums[i + 1]:
        i += 1
    if i == 0 or i == n - 1:
        return False

    while i + 1 < n and nums[i] > nums[i + 1]:
        i += 1
    if i == n - 1:
        return False

    while i + 1 < n and nums[i] < nums[i + 1]:
        i += 1

    return i == n - 1


nums = [1, 3, 2, 4, 5]
print(isTrionic(None, nums))
