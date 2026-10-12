# A implementação percorre os índices do vetor e verifica quais são divisores do tamanho da lista. Quando o tamanho n é divisível por x + 1, o quadrado do elemento naquela posição é somado à variável ans. Ao final, retorna a soma dos quadrados de todos os elementos cujos índices (considerando a contagem a partir de 1) são divisores do tamanho do vetor.

from typing import List


def sumOfSquares(self, nums: List[int]) -> int:
    n = len(nums)
    ans = 0
    for x in range(n):
        if n % (x + 1) == 0:
            ans += nums[x]**2
    return ans


nums = [1, 2, 3, 4, 5]
result = sumOfSquares(None, nums)
