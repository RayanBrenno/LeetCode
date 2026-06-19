# A ideia é percorrer o vetor gain simulando a altitude em cada ponto da viagem. A variável aux guarda a altitude atual (acumulando os ganhos e perdas), enquanto ans armazena a maior altitude alcançada até o momento. A cada elemento, atualizamos a altitude atual somando o ganho correspondente e depois verificamos se ela supera a maior altitude registrada. No final, retornamos o maior valor encontrado.

from typing import List

def largestAltitude(self, gain: List[int]) -> int:
    aux, ans = 0, 0

    for x in gain:
        aux += x
        ans = max(ans, aux)

    return ans


gain = [-5, 1, 5, 0, -7]
print(largestAltitude(None, gain))