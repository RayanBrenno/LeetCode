# O algoritmo percorre as teclas pressionadas para descobrir qual teve a maior duração de pressionamento. Inicialmente, considera que a primeira tecla é a mais lenta, usando releaseTimes[0] como tempo máximo e keysPressed[0] como resposta inicial. Em seguida, percorre as demais teclas calculando o tempo que cada uma ficou pressionada, obtido pela diferença entre o tempo de liberação atual e o anterior (releaseTimes[x] - releaseTimes[x-1]). Se esse tempo for maior que o maior tempo registrado, a tecla atual passa a ser a nova resposta. Caso o tempo seja igual ao máximo, é escolhida a tecla lexicograficamente maior (a que vem depois no alfabeto). Ao final da iteração, o algoritmo retorna a tecla que teve a maior duração de pressionamento.

from typing import List

def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
    max_time = releaseTimes[0]
    ans = keysPressed[0]

    for x in range(1, len(keysPressed)):
        aux = releaseTimes[x] - releaseTimes[x-1]

        if aux > max_time or (aux == max_time and keysPressed[x] > ans):
            max_time = aux
            ans = keysPressed[x]

    return ans


releaseTimes = [9, 29, 49, 50]
keysPressed = "cbcd"
print(slowestKey(releaseTimes, keysPressed))