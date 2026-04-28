# Criamos três conjuntos representando as linhas do teclado. Para cada palavra, convertemos para minúsculo e usamos a primeira letra para identificar qual linha ela deveria seguir. Depois verificamos se todas as letras pertencem à mesma linha usando all(). Se pertencerem, adicionamos a palavra na resposta.

from typing import List

def findWords(self, words: List[str]) -> List[str]:
    row1 = set("qwertyuiop")
    row2 = set("asdfghjkl")
    row3 = set("zxcvbnm")

    ans = []

    for word in words:
        lower_word = word.lower()

        if lower_word[0] in row1:
            row = row1
        elif lower_word[0] in row2:
            row = row2
        else:
            row = row3

        if all(char in row for char in lower_word):
            ans.append(word)

    return ans


words = ["Hello", "Alaska", "Dad", "Peace"]
print(findWords(None, words))