# O código percorre cada query e, para cada uma, atualiza os valores do array multiplicando elementos em posições específicas (de l até r, pulando de k em k) pelo valor v, sempre aplicando módulo . Depois de aplicar todas as queries, ele percorre o array final e calcula o XOR entre todos os elementos, retornando esse resultado.

from typing import List

def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
    MOD = 10**9 + 7

    for l, r, k, v in queries:
        for x in range(l, r + 1, k):
            nums[x] = (nums[x] * v) % MOD

    ans = 0
    for x in nums:
        ans ^= x

    return ans


nums = [1, 2, 3, 4, 5]
queries = [[0, 4, 1, 2], [0, 3, 2, 3], [1, 2, 1, 4]]
print(xorAfterQueries(None, nums, queries))