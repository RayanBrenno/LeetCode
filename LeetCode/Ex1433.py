# A ideia é ordenar as duas strings para comparar suas letras na mesma posição, verificando se uma delas é sempre maior ou igual à outra em todas as posições. Utilizamos all() junto com zip() para garantir que todas as comparações sejam verdadeiras em pelo menos uma das direções, determinando se uma string consegue quebrar a outra.


def checkIfCanBreak(self, s1: str, s2: str) -> bool:
    s1 = sorted(s1)
    s2 = sorted(s2)
    return all(x >= y for x, y in zip(s1, s2)) or all(x >= y for x, y in zip(s2, s1))


s1 = "abc"
s2 = "xya"
print(checkIfCanBreak(None, s1, s2))
