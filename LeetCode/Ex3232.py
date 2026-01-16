# A lógica aqui é separar os números em dois grupos. Primeiro, o array é ordenado para garantir que os valores até 9 venham antes. Em seguida, somam-se apenas os números menores ou iguais a 9, parando quando aparecem valores maiores. No final, compara-se essa soma com a soma do restante do array; se os dois valores forem diferentes, Alice vence, caso contrário, não.

from typing import List
def canAliceWin(self, nums: List[int]) -> bool:
    nums.sort()
    aux = 0
    for x in nums:
        if x > 9:
            break
        aux += x

    return aux != sum(nums)-aux

print(canAliceWin(None, [1,2,3,4,5]))
print(canAliceWin(None, [10,11,12,13]))