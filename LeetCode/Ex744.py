#  A ideia do exercício é percorrer a lista de letras (que já está ordenada) e retornar a primeira letra que seja maior que o target. Assim que encontra uma letra com valor maior (comparando pelo código ASCII), ela é retornada. Se nenhuma letra for maior que o target, o algoritmo retorna a primeira letra da lista, simulando o comportamento circular do problema.

from typing import List

def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    for x in letters:
        if ord(x) > ord(target):
            return x
    return letters[0]

letters = ["c", "f", "j"]
target = "a"
print(nextGreatestLetter(None, letters, target))