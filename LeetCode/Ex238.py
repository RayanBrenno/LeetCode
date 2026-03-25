# Esse exercício retorna um array onde cada posição contém o produto de todos os elementos do array original, exceto o próprio, sem usar divisão. Para isso, ele usa a ideia de prefixo e sufixo. Primeiro, percorre o array de trás pra frente guardando em cada posição o produto dos elementos à direita (suffix). Depois, percorre da frente pra trás multiplicando esse valor pelo produto dos elementos à esquerda (prefix). Assim, cada posição recebe o produto de todos os outros elementos, de forma eficiente e sem recalcular tudo várias vezes.

from typing import List

def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    ans = [0] * n

    suffix = 1
    for x in range(n-1, -1, -1):
        ans[x] = suffix
        suffix *= nums[x]

    prefix = 1
    for x in range(n):
        ans[x] = ans[x] * prefix
        prefix *= nums[x]

    return ans


nums = [1,2,3,4]
print(productExceptSelf(None, nums))