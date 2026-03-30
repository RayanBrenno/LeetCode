# Esse código verifica se duas strings podem ser consideradas equivalentes separando os caracteres por posição par e ímpar. Ele conta quantas vezes cada caractere aparece nas posições pares de s1 e s2 e compara esses contadores; depois faz o mesmo para as posições ímpares. Se os dois pares de contagens forem iguais, retorna True, caso contrário False.

from collections import Counter

def areSimilar(s1, s2):

    return Counter(s1[::2]) == Counter(s2[::2]) and \
        Counter(s1[1::2]) == Counter(s2[1::2])

    # if len(s1) != len(s2):
    #     return False

    # even1, even2 = {}, {}
    # odd1, odd2 = {}, {}

    # for x in range(len(s1)):
    #     if x % 2 == 0:
    #         even1[s1[x]] = even1.get(s1[x], 0) + 1
    #         even2[s2[x]] = even2.get(s2[x], 0) + 1
    #     else:
    #         odd1[s1[x]] = odd1.get(s1[x], 0) + 1
    #         odd2[s2[x]] = odd2.get(s2[x], 0) + 1

    # return even1 == even2 and odd1 == odd2


s1 = "abcde"
s2 = "bacde"
print(areSimilar(s1, s2))
