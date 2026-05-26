# Conta os caracteres especiais numa string: um caractere é "especial" se aparece tanto em maiúsculo quanto minúsculo. Usa um Counter pra mapear os caracteres presentes, depois itera sobre eles checando se cada letra maiúscula tem sua versão minúscula correspondente no mesmo mapa. Retorna a contagem total desses pares.

from collections import Counter

def numberOfSpecialChars(self, word: str) -> int:
    ans = 0
    count = Counter(word)
    keys = count.keys()
    for x in keys:
        if x.isupper() and x.lower() in keys:
            ans += 1

    return ans


# Exemplo de uso:
word = "aAAbbbb"
print(numberOfSpecialChars(None, word))  # Output: 1