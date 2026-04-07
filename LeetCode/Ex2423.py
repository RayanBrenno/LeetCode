# A gente conta quantas vezes cada letra aparece e depois tenta remover uma letra de cada vez. A cada remoção, verifica se todas as frequências que sobraram são iguais (usando um set). Se em alguma tentativa todas forem iguais, retorna True; se nenhuma funcionar, retorna False.

from collections import Counter

def equalFrequency(self, word: str) -> bool:

    for x in range(len(word)):
        temp = word[:x] + word[x+1:]
        freq = Counter(temp)

        values = list(freq.values())

        if len(set(values)) == 1:
            return True

    return False


word = "abcc"
print(equalFrequency(None, word))
