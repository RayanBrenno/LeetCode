# A função simula colisões entre asteroides usando uma pilha (stack). Ela percorre a lista e, para cada asteroide, verifica se há uma possível colisão — isso acontece quando o asteroide atual é negativo (indo para a esquerda) e o topo da pilha é positivo (indo para a direita). Enquanto houver colisão, compara os tamanhos: se o asteroide atual for maior (em valor absoluto), o topo da pilha é removido e a verificação continua; se forem iguais, ambos se destroem (remove o topo e para); se o da pilha for maior, o atual é destruído e o loop é interrompido. Caso não ocorra colisão, o asteroide é adicionado à pilha. No final, a pilha representa os asteroides restantes após todas as colisões.

from typing import List


def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    stack = []

    for x in asteroids:
        while stack and x < 0 < stack[-1]:
            if -x > stack[-1]:
                stack.pop()
                continue
            elif -x == stack[-1]:
                stack.pop()
            break
        else:
            stack.append(x)
    return stack


asteroids = [5, 10, -5]
print(asteroidCollision(None, asteroids))