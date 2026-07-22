# Essa solução converte cada número do vetor para string e utiliza join para concatenar todos eles em uma única sequência de caracteres. Em seguida, percorre cada caractere dessa sequência e o converte novamente para int por meio de uma list comprehension, formando o vetor resposta. Dessa forma, todos os dígitos são separados e adicionados na mesma ordem em que aparecem nos números originais, resultando em uma implementação simples e concisa.

from typing import List


def separateDigits(self, nums: List[int]) -> List[int]:

    # ans = []
    # for x in reversed(nums):
    #     while x > 0:
    #         ans.insert(0, x % 10)
    #         x //= 10

    # return ans
    
    return [int(x) for x in "".join(str(x) for x in nums)]


nums = [13, 25, 83, 77]
print(separateDigits(None, nums))  # Output: [1, 3, 2, 5, 8, 3, 7, 7]
