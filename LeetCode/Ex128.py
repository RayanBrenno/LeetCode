# Transforma o array em um set para remover duplicados e depois ordena os números, percorrendo a lista para contar quantos elementos consecutivos existem em sequência; quando encontra uma quebra, atualiza o maior tamanho encontrado e reinicia a contagem, tratando também o caso de array vazio e garantindo no final que a última sequência seja considerada.

from typing import List


def longestConsecutive(self, nums: List[int]) -> int:
    if not nums:
        return 0

    nums = sorted(set(nums))
    ans, aux = 0, 1

    for x in range(len(nums) - 1):
        if nums[x] + 1 == nums[x + 1]:
            aux += 1
        else:
            ans = max(ans, aux)
            aux = 1

    return max(ans, aux)


nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(None, nums))  # Output: 4
