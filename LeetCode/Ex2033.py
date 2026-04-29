# Esse código resolve o problema transformando a matriz em uma lista única (nums) para facilitar o processamento. Primeiro, ele pega o resto da divisão do primeiro número por x e verifica se todos os outros possuem o mesmo resto — isso é necessário porque, se algum número tiver resto diferente, nunca será possível igualar todos usando operações de ±x, então retorna -1. Se for possível, ele ordena os números e escolhe a mediana (mid_num) como valor alvo, porque a mediana minimiza a soma das distâncias absolutas. Depois, calcula quantas operações cada número precisa para chegar até essa mediana (abs(mid_num - num) // x) e soma tudo em ans. No final, retorna o total mínimo de operações necessárias para deixar todos os elementos iguais.

from typing import List

def minOperations(self, grid: List[List[int]], x: int) -> int:
    nums = []
    ans = 0

    for aux in grid:
        nums.extend(aux)

    remainder = nums[0] % x
    for num in nums:
        if num % x != remainder:
            return -1

    nums.sort()
    n = len(nums)
    mid_index = n // 2
    mid_num = nums[mid_index]

    for num in nums:
        ans += abs(mid_num - num) // x

    return ans


grid = [[2, 4], [6, 8]]
x = 2
print(minOperations(None, grid, x))
