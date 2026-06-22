# O código conta quantas vezes cada letra aparece na string usando Counter e depois calcula quantas vezes é possível formar a palavra "balloon". Como as letras "l" e "o" aparecem duas vezes na palavra, suas quantidades são divididas por 2 (// 2). O resultado é o menor valor entre as quantidades necessárias de cada letra, pois a letra mais escassa limita o número máximo de palavras "balloon" que podem ser montadas.

from typing import Counter

def maxNumberOfBalloons(self, text: str) -> int:
    count = Counter(text)
    return min(count["b"], count["a"], count["l"]//2, count["o"]//2, count["n"])


text = "loonbalxballpoon"
print(maxNumberOfBalloons(None, text))  # Output: 2