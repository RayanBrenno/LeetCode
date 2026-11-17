# A implementação percorre todos os índices iniciais e testa os subarrays com tamanhos entre l e r, calculando a soma de cada um. Quando encontra uma soma positiva, atualiza ans caso seja menor que o valor armazenado. Ao final, retorna a menor soma positiva encontrada ou -1 caso nenhum subarray válido exista.


from typing import List


def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
    ans = float('inf')

    for x in range(len(nums)):
        for y in range(l, r + 1):
            if x + y <= len(nums):
                total = sum(nums[x:x+y])

                if total > 0:
                    ans = min(ans, total)

    return ans if ans != float('inf') else -1


nums = [1, -2, 3, 4, -5]
l = 2
r = 3
print(minimumSumSubarray(None, nums, l, r))