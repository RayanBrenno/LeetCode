# A função verifica se a lista contém exatamente os números 1, 2, 3 até n sem faltar nenhum. Ela ordena a lista primeiro, depois valida que cada posição x tem o valor x+1 para todos os elementos até o penúltimo, e por fim verifica se o último elemento é igual a n. Basicamente é um cheque para confirmar que tem todos os números sequenciais do 1 ao tamanho da lista.

from typing import List

def isGood(self, nums: List[int]) -> bool:
    nums.sort()
    n = len(nums) - 1

    for x in range(n):
        if nums[x] != x + 1:
            return False

    return nums[n] == n


nums = [1, 2, 3]
print(isGood(nums))  # Output: True