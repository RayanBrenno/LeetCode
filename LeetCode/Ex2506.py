# A ideia é usar o Counter para contar quantas palavras possuem o mesmo conjunto de caracteres únicos. Para isso, usamos frozenset(word), que funciona como um set, removendo os caracteres repetidos, mas sendo imutável e podendo ser usado como chave no Counter. Assim, palavras como "aba" e "aab" são consideradas iguais, pois possuem os mesmos caracteres únicos. Depois, percorremos as frequências de cada conjunto e usamos a fórmula num * (num - 1) // 2 para calcular quantos pares podem ser formados com as palavras de cada grupo, somando os resultados em ans.

from collections import Counter
from typing import List


def similarPairs(self, words: List[str]) -> int:

    aux = Counter(frozenset(word) for word in words)
    ans = 0

    for num in aux.values():
        ans += num * (num - 1) // 2

    return ans

    # ans = 0

    # for x in range(len(words)):
    #     for y in range(x + 1, len(words)):
    #         if set(words[x]) == set(words[y]):
    #             ans += 1

    # return ans


words = ["aba", "aabb", "abcd", "bac", "aabc"]
result = similarPairs(None, words)
print(result)  # Output: 2
