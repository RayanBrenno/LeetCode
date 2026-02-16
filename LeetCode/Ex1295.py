# Ele percorre a lista nums e, para cada número, calcula quantos dígitos ele tem aumentando aux enquanto x for maior ou igual a 10**aux. Isso basicamente conta a quantidade de casas decimais do número. Depois verifica se essa quantidade é par (aux % 2 == 0) e, se for, incrementa ans. No final, retorna quantos números da lista possuem quantidade par de dígitos

from typing import List


def findNumbers(self, nums: List[int]) -> int:
    ans = 0
    for x in nums:
        aux = 1
        while x >= 10**aux:
            aux += 1
        ans += 1 if aux % 2 == 0 else 0
    return ans

    # ans = 0
    # for num in nums:
    #     if len(str(num)) % 2 == 0:
    #         ans += 1
    # return ans


nums = [12, 345, 2, 6, 7896]
print(findNumbers(None, nums))
