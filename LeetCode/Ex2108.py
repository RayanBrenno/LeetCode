# O código percorre a lista de palavras e verifica cada uma para ver se é um palíndromo (ou seja, se é igual à sua versão invertida). Assim que encontra a primeira palavra que satisfaz essa condição, ele a retorna imediatamente. Caso nenhuma palavra seja palíndromo, retorna uma string vazia.

from typing import List

def firstPalindrome(self, words: List[str]) -> str:

    for x in words:
        if x == x[::-1]:
            return x

    return ""


words = ["abc", "car", "ada", "racecar", "cool"]
print(firstPalindrome(None, words))