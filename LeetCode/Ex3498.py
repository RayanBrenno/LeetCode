# A implementação percorre cada caractere da string e calcula seu valor pelo grau reverso, usando 123 - ord(x) para transformar as letras de a a z em valores de 26 a 1. Esse valor é multiplicado pela posição do caractere na string, começando em 1, e acumulado em ans, que é retornado ao final.


def reverseDegree(self, s: str) -> int:
    ans, index = 0, 1
    for x in s:
        ans += (123 - ord(x)) * index
        index += 1

    return ans

    # return sum(((123 - ord(char)) * (index + 1)) for index, char in enumerate(s))


s = "abc"
print(reverseDegree(s))  # Saída: 148