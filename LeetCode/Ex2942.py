# A implementação percorre a lista words usando enumerate para obter o índice e cada palavra, adicionando à lista resultante apenas os índices das palavras que contêm o caractere x.

from typing import List

def findWordsContaining(self, words: List[str], x: str) -> List[int]:
    return [index for index, word in enumerate(words) if x in word]


words = ["apple", "banana", "cherry", "date"]
x = "an"