# Você ordena os preços e percorre do maior para o menor, simulando a promoção onde a cada três itens o mais barato é grátis; usa um contador pra controlar isso, somando dois itens e pulando o terceiro, garantindo que sempre paga pelos dois mais caros e ignora o mais barato — assim minimiza o custo total de forma eficiente.

from typing import List


def minimumCost(self, cost: List[int]) -> int:
    cost.sort()
    ans = 0
    count = 0
    for x in reversed(cost):
        if count == 2:
            count = 0
            continue
        ans += x
        count += 1

    return ans


cost = [1, 2, 3]
print(minimumCost(None, cost))