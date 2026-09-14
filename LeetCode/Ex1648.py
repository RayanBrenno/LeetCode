# A implementação ordena o inventário em ordem decrescente e percorre os valores da esquerda para a direita, pegando o nível atual e o próximo para descobrir quantos produtos estão naquele intervalo. Assim, em vez de vender item por item, calcula de uma vez o valor de todos os produtos daquele nível, multiplicando pela quantidade de itens e somando em ans. Quando os pedidos não completam um nível inteiro, divide a quantidade de pedidos entre os produtos disponíveis, calcula as rodadas completas e depois soma os pedidos restantes individualmente.

from typing import List


def maxProfit(self, inventory: List[int], orders: int) -> int:
    inventory.sort(reverse=True)
    ans = 0
    n = len(inventory)

    for x in range(n):
        aux = inventory[x]
        aux2 = inventory[x + 1] if x + 1 < n else 0

        count = (aux - aux2) * (x + 1)

        if orders >= count:
            ans += (aux + aux2 + 1) * (aux - aux2) * (x + 1) // 2
            orders -= count
        else:
            q = orders // (x + 1)
            r = orders % (x + 1)

            ans += (aux + aux - q + 1) * q * (x + 1) // 2
            ans += (aux - q) * r
            break

    return ans % (10**9 + 7)


inventory = [2, 5]
orders = 4
print(maxProfit(inventory, orders))  # Saída: 14