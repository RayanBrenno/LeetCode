# Percorre cada palavra da lista e calcula a soma dos pesos de suas letras usando o array weights. Em seguida, transforma essa soma em uma nova letra, calculando aux % 26 e subtraindo o resultado da letra 'z'. Cada letra gerada é adicionada à resposta e, ao final, todas são concatenadas para formar a string final.

from typing import List

def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
    ans = []
    for word in words:
        aux = 0
        for x in word:
            aux += weights[ord(x) - ord("a")]
        ans.append(chr(ord("z") - aux % 26))
    return "".join(ans)


words = ["abc", "bcd", "cde"]
weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
print(mapWordWeights(None, words, weights))  # Output: "xwz"