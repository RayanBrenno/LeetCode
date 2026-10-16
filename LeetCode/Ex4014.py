# A implementação ordena os preços e os descontos em ordem decrescente para aplicar os maiores descontos aos produtos mais caros. Depois, percorre a quantidade de pares possíveis, calcula o preço com desconto de cada produto usando a porcentagem correspondente e, por fim, retorna a soma de todos os preços.

from typing import List

def minPrice(self, prices: List[int], discounts: List[int]) -> float:

    prices.sort(reverse=True)
    discounts.sort(reverse=True)
    a, b = len(prices), len(discounts)
    for x in range(min(a, b)):
        prices[x] = (prices[x] * (100 - discounts[x])) / 100

    return sum(prices)


prices = [100, 200, 300]
discounts = [10, 20]
print(minPrice(prices, discounts))  # Output: 470.0