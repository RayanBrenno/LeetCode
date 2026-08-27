# A primeira implementação percorre os dígitos do número da esquerda para a direita usando divisão inteira e módulo para identificar o primeiro 6; quando encontra, soma 3 * 10^posição para transformá-lo em 9, garantindo o maior número possível. Caso não exista 6, retorna o próprio número. A segunda faz a mesma lógica convertendo o número para uma lista de caracteres, substitui o primeiro "6" por "9" e depois transforma a lista novamente em inteiro.*

def maximum69Number(self, num: int) -> int:
    n = len(str(num))
    for x in range(n):
        aux = (num // 10**(n-x-1)) % 10
        if aux == 6:
            return num + (3 * 10**(n-x-1))

    return num

    # aux = list(str(num))
    # for x in range(len(aux)):
    #     if aux[x] == "6":
    #         aux[x] = "9"
    #         break
    # return int("".join(aux))


num = 9669
print(maximum69Number(None, num))  # Output: 9969