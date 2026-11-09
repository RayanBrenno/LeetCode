# A implementação utiliza um set para armazenar os pares de caracteres consecutivos encontrados na string. A cada iteração, verifica se o par atual invertido já existe no set ou se os dois caracteres são iguais; caso alguma condição seja satisfeita, retorna True. Caso contrário, adiciona o par atual ao set e continua. Se nenhum par correspondente for encontrado, retorna False.


def isSubstringPresent(self, s: str) -> bool:
    aux = set()

    for x in range(len(s) - 1):
        if s[x+1] + s[x] in aux or s[x+1] == s[x]:
            return True
        else:
            aux.add(s[x] + s[x+1])

    return False

    # aux1 = []
    # for x,y in pairwise(s):
    #     aux1.append(x+y)

    # aux2 = []
    # for x,y in pairwise(s[::-1]):
    #     aux2.append(x+y)

    # return len(set(aux1) & set(aux2)) > 0


s = "abccba"
print(isSubstringPresent(None, s))
