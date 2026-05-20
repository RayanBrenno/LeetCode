# Conta as ocorrências de cada lâmpada e retorna as que aparecem um número ímpar de vezes, já ordenadas.

from collections import Counter


def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
    return sorted(x for x, c in Counter(bulbs).items() if c % 2 != 0)


bulbs = [1, 2, 3, 2, 3, 1, 3]
print(toggleLightBulbs(None, bulbs))
