# Percorremos o array procurando os valores 1. Mantemos o índice do último 1 encontrado e, sempre que encontramos outro, calculamos quantas posições existem entre eles. Se essa quantidade for menor que k, significa que dois 1s estão próximos demais e retornamos False. Caso contrário, atualizamos a posição do último 1 e continuamos a busca. Se o percurso terminar sem encontrar nenhuma violação, retornamos True.

from typing import List

def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = -1

        for i, x in enumerate(nums):
            if x == 1:
                if prev != -1 and i - prev - 1 < k:
                    return False
                prev = i

        return True
    
    
nums = [1, 0, 0, 1, 0, 1]
k = 2
print(kLengthApart(None, nums, k))