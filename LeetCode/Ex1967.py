# O algoritmo percorre todas as strings de patterns e verifica se cada uma delas aparece como substring em word usando o operador in. Sempre que uma substring é encontrada, incrementa um contador. Ao final da iteração, retorna esse contador, que representa a quantidade de padrões presentes na palavra.

from typing import List

def numOfStrings(self, patterns: List[str], word: str) -> int:
    ans = 0
    for x in patterns:
        if x in word:
            ans += 1

    return ans


patterns = ["a", "abc", "bc", "d"]
word = "abc"
print(numOfStrings(None, patterns, word))