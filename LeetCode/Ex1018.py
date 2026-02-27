# A ideia do exercício é percorrer a lista de bits construindo o número binário do prefixo de forma incremental. A cada novo bit, o valor atual é multiplicado por 2 (shift para a esquerda) e somado ao bit, simulando a formação do número em binário. Em vez de armazenar o número completo, o algoritmo mantém apenas o resto da divisão por 5, já que para saber se é divisível por 5 só importa se o resto é zero. Assim, ele evita números grandes e consegue verificar em cada passo se o prefixo atual é divisível por 5, retornando uma lista de booleanos. Complexidade O(n).

from typing import List

def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
    ans = []
    prefix = 0
    for x in nums:
        prefix = ((prefix << 1)+x) % 5
        ans.append(prefix == 0)

    return ans


nums = [0,1,1]
print(prefixesDivBy5(None, nums))