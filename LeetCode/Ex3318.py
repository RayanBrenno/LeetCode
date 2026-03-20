# Esse algoritmo percorre o array usando uma janela deslizante de tamanho k, e para cada subarray ele conta quantas vezes cada número aparece. Em seguida, ordena esses números primeiro pela maior frequência e, em caso de empate, pelo maior valor numérico. Depois disso, seleciona os x elementos mais relevantes dessa ordenação (ou seja, os mais frequentes e maiores) e calcula uma soma ponderada, multiplicando cada número pela sua quantidade de ocorrências. Esse valor é adicionado à lista de resposta, que ao final contém o resultado para todas as janelas possíveis do array.

from typing import Counter
from git import List


def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
    ans = []
    n = len(nums)
    for i in range(n - k + 1):
        count = Counter(nums[i:i+k])
        count = sorted(count.items(), key=lambda item: (-item[1], -item[0]))
        aux_sum = sum(num * reps for num, reps in count[:x])
        ans.append(aux_sum)

    return ans


nums = [1, 2, 2, 3, 3, 3]
k = 3
x = 2
print(findXSum(None, nums, k, x))