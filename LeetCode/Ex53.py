# A função implementa o algoritmo de Kadane para encontrar a maior soma possível de um subarray contínuo: ela percorre a lista acumulando os valores em aux, que representa a soma do trecho atual, e a cada passo atualiza ans com o maior valor já encontrado; se em algum momento essa soma acumulada se torna negativa, ela é resetada para zero, pois continuar com um valor negativo só prejudicaria qualquer soma futura, garantindo assim que sempre se considera apenas trechos que podem maximizar o resultado final.

from typing import List

def maxSubArray(self, nums: List[int]) -> int:
    aux = 0
    ans = float("-inf")

    for x in nums:
        aux += x
        ans = max(ans, aux)
        if aux < 0:
            aux = 0

    return ans


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(None, nums))