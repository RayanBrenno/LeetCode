# O código calcula quanto tempo leva para a pessoa na posição k terminar de comprar seus tickets sem simular a fila diretamente. Ele pega quantos tickets essa pessoa precisa (target) e percorre toda a lista somando quantas vezes cada pessoa consegue comprar antes dela terminar. Para quem está antes ou na posição k, cada um contribui até no máximo target, pois participa de todas as rodadas até o fim. Já quem está depois de k só pode contribuir até target - 1, porque quando chega a última compra da pessoa k, essas pessoas não entram mais na rodada. No final, a soma dessas contribuições representa o tempo total.

from typing import List

def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
    
    ans = 0
    target = tickets[k]

    for x in range(len(tickets)):
        if x <= k:
            ans += min(tickets[x], target)
        else:
            ans += min(tickets[x], target - 1)

    return ans


# n = len(tickets)
# ans = 0

# if tickets[k] == 1:
#     return k + 1

# while tickets[k] > 0:
#     for x in range(n):
#         if tickets[x] > 0:
#             tickets[x] -= 1
#             ans += 1

#         if tickets[k] == 0:
#             return ans

# return ans

tickets = [2, 3, 2]
k = 2
print(timeRequiredToBuy(tickets, k))