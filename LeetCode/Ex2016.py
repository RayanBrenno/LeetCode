# A ideia é percorrer o vetor mantendo o menor valor encontrado até o momento (aux), que representa o melhor candidato para iniciar a diferença. Para cada elemento seguinte, se ele for maior que esse menor valor, calculamos a diferença e atualizamos a maior resposta encontrada (ans). Caso contrário, significa que encontramos um novo menor valor, então atualizamos aux para aumentar as chances de obter uma diferença maior nos próximos elementos. Ao final, retornamos a maior diferença válida encontrada ou -1 caso não exista nenhum par em que o maior elemento apareça depois do menor.

from typing import List

def maximumDifference(self, nums: List[int]) -> int:
    n = len(nums)
    ans, aux = -1, nums[0]

    for x in range(1, n):
        if nums[x] > aux:
            ans = max(ans, nums[x] - aux)
        else:
            aux = nums[x]

    return ans


nums = [7, 1, 5, 4]
print(maximumDifference(None, nums))  # Output: 4