# A implementação primeiro verifica se comprar os dois tipos de itens separadamente é mais barato ou igual a comprar um item compartilhado, retornando esse custo caso seja. Caso contrário, utiliza o máximo possível de itens compartilhados para atender simultaneamente às duas necessidades e, depois, completa o requisito que ainda falta escolhendo entre o item individual e o compartilhado, sempre priorizando a opção mais barata.


def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
    ans = 0

    if cost1 + cost2 <= costBoth:
        ans = cost1 * need1 + cost2 * need2
    else:
        min_qtd = min(need1, need2)
        ans += costBoth * min_qtd
        need1 -= min_qtd
        need2 -= min_qtd

        if need1 > 0:
            ans += min(cost1, costBoth) * need1
        else:
            ans += min(cost2, costBoth) * need2

    return ans


cost1 = 2
cost2 = 3
costBoth = 4
need1 = 3
need2 = 2
print(minimumCost(None, cost1, cost2, costBoth, need1, need2))