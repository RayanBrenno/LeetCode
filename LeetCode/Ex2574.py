# Primeiro, cria um array de soma prefixada (ans), onde cada posição guarda a soma dos elementos da esquerda até ela. Depois, percorre o array de trás para frente calculando a soma dos elementos da direita até cada posição e substitui ans[x] pela diferença absoluta entre a soma da esquerda e a soma da direita. Ao final, retorna o array com as diferenças absolutas entre as somas dos lados esquerdo e direito de cada índice.

from typing import List

def leftRightDifference(self, nums: List[int]) -> List[int]:
    ans = []
    aux = 0
    for x in nums:
        aux += x
        ans.append(aux)

    n = len(nums)
    aux = 0
    for x in range(n-1, -1, -1):
        aux += nums[x]
        ans[x] = abs(ans[x] - aux)

    return ans


nums = [10, 4, 8, 3]
print(leftRightDifference(None, nums))  # Output: [15, 1, 11, 22]
