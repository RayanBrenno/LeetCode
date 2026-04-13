# A função percorre a lista procurando os índices onde o valor é igual ao target e, para cada ocorrência, calcula a distância absoluta entre esse índice e a posição start. Ela mantém a menor distância encontrada até o momento e, se perceber que a nova distância ficou maior que a anterior, retorna imediatamente a menor já encontrada. No final, caso não haja interrupção antecipada, retorna a menor distância entre start e qualquer ocorrência de target na lista.

from typing import List


def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
    ans = float('inf')

    for index, num in enumerate(nums):
        if num == target:
            aux = ans
            ans = abs(index-start)
            if aux < ans:
                return aux

    return ans


nums = [1,2,3,4,5]
target = 5
start = 3
print(getMinDistance(None, nums, target, start))