#A ideia do exercício é, para cada número do array, tentar descobrir se ele pode ser formado pelo OR bit a bit entre dois números consecutivos (y e y+1). Para isso, o algoritmo testa todos os valores possíveis de y menores que x e verifica se y | (y+1) resulta em x. Se encontrar um valor válido, ele é adicionado à resposta; caso contrário, retorna -1 para aquele número.

from typing import List

def minBitwiseArray(self, nums: List[int]) -> List[int]:
    ans = []

    for x in nums:
        aux = -1
        for y in range(1, x):
            if y | (y+1) == x:
                aux = y
                break
        ans.append(aux)
        
    return ans


nums = [2, 3, 5, 7]
print(minBitwiseArray(None, nums)) 