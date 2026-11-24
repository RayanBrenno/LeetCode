# A implementação percorre todas as possíveis subarrays utilizando dois loops, onde x define o início e y percorre os elementos seguintes. Durante a expansão, atualiza o produto, o MDC e o MMC da subarray e verifica se o produto é igual ao MDC multiplicado pelo MMC. Quando a condição é satisfeita, atualiza ans com o maior tamanho encontrado.

from typing import List


def maxLength(self, nums: List[int]) -> int:
    ans = 1

    for x in range(len(nums)):
        product = nums[x]
        g = nums[x]
        l = nums[x]
        for y in range(x + 1, len(nums)):
            product *= nums[y]
            g = gcd(g, nums[y])
            l = lcm(l, nums[y])
            if product == g * l:
                ans = max(ans, y - x + 1)

    return ans


nums = [1, 2, 1, 2, 1, 1, 1]
print(maxLength(None, nums))
