# Você ordena as moedas e vai construindo o maior intervalo contínuo de valores que consegue formar começando do 1. A variável res representa o próximo valor que ainda não dá pra formar. Se a moeda atual for menor ou igual a res, você consegue estender o intervalo somando ela (res += a). Se for maior, aparece um “buraco” e você para, porque não dá pra formar aquele valor. No final, res é exatamente o menor valor impossível de formar.

from typing import List

def getMaximumConsecutive(self, coins: List[int]) -> int:
    coins.sort()
    ans = 1
    for x in coins:
        if x > ans:
            return ans
        ans += x

    return ans


coins = [1, 3]
print(getMaximumConsecutive(None, coins))
