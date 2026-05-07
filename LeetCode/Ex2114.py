# O código percorre cada frase da lista sentences e conta quantas palavras ela possui. Como as palavras são separadas por espaços, ele usa count(" ") + 1 para descobrir a quantidade de palavras da frase atual. Durante o percurso, ans guarda o maior valor encontrado. No final, retorna a quantidade máxima de palavras entre todas as frases.

from typing import List

def mostWordsFound(self, sentences: List[str]) -> int:
    ans = 0
    for x in sentences:
        ans = max(ans, x.count(" ")+1)
    return ans


sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
print(mostWordsFound(sentences))