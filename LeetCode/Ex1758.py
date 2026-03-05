# A ideia é criar as duas possíveis strings alternadas do mesmo tamanho de s: uma começando com "0" ("0101...") e outra começando com "1" ("1010..."). Depois o código percorre as três strings ao mesmo tempo usando zip e conta quantos caracteres de s são iguais a cada padrão. Como em Python True vale 1 e False vale 0, a expressão count += x == y soma quando os caracteres são iguais. No final, ele retorna o menor valor entre os dois contadores, representando o menor número de operações necessárias para transformar s em uma string alternada.

def minOperations(self, s: str) -> int:
    n = len(s)
    aux1 = "01"*(n//2) if n % 2 == 0 else "01"*(n//2) + "0"
    aux2 = "10"*(n//2) if n % 2 == 0 else "10"*(n//2) + "1"
    count_aux1 = 0
    count_aux2 = 0
    for x, y, z in zip(s, aux1, aux2):
        count_aux1 += x == y
        count_aux2 += x == z
    return min(count_aux1, count_aux2)


s = "0100"
print(minOperations(None, s))