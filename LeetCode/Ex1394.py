# Conta a frequência de cada número com Counter e percorre os valores distintos. Sempre que encontra um número cuja frequência é igual ao próprio valor (count[x] == x), atualiza a resposta com o maior deles. Ao final, retorna o maior número "sortudo" encontrado ou -1 caso nenhum satisfaça a condição.

from typing import List
from collections import Counter

def findLucky(self, arr: List[int]) -> int:
    count = Counter(arr)
    ans = -1
    for x in count:
        if count[x] == x and x > ans:
            ans = x

    return ans

arr = [2, 2, 3, 4]
print(findLucky(None, arr))