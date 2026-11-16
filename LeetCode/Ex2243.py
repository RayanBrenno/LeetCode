# A implementação divide a string em grupos de tamanho k, soma os dígitos de cada grupo e armazena os resultados em uma nova string. Esse processo é repetido enquanto o tamanho da string for maior que k, até que ela tenha no máximo k caracteres, retornando o resultado final.


def digitSum(self, s: str, k: int) -> str:
    while len(s) > k:
        aux1 = []
        for x in range(0, len(s), k):
            aux2 = 0
            for y in s[x:x+k]:
                aux2 += int(y)
            aux1.append(str(aux2))
        s = "".join(aux1)

    return s


s = "11111222223"
k = 3
print(digitSum(None, s, k))
