# O código percorre todos os bits do número enquanto ele for maior que 0, usando n & 1 para verificar se o bit atual é 1. Se for, ele checa se a posição é par ou ímpar através de um índice e incrementa o contador correspondente (even ou odd). A cada passo, usa n >>= 1 para deslocar o número pra direita e analisar o próximo bit. No final, retorna a quantidade de bits 1 nas posições pares e ímpares.

from typing import List

def evenOddBit(self, n: int) -> List[int]:
    even, odd = 0, 0
    even_char = True
    while n > 0:
        if n & 1 == 1 and even_char:
            even += 1
        elif n & 1 == 1 and not even_char:
            odd += 1

        even_char = False if even_char else True
        n >>= 1

    return [even, odd]


n = 17
print(evenOddBit(None, n))
