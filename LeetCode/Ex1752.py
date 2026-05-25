# A solução consiste em contar quantas "quedas" existem na sequência, ou seja, posições onde um elemento é maior que o próximo. Numa array válida só pode existir no máximo uma queda, pois a rotação cria apenas um ponto de quebra na ordenação. O truque do % n garante que o último elemento seja comparado com o primeiro, fechando o ciclo da rotação.

from typing import List

def check(self, nums: List[int]) -> bool:
        drops = 0
        n = len(nums)
        
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                drops += 1
            if drops > 1:
                return False
        
        return True
    

# Exemplo de uso:
nums = [3, 4, 5, 1, 2]
print(check(None, nums))  # Output: True