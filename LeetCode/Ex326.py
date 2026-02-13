# Esse código verifica se um número é potência de 3. Primeiro ele checa se n é menor ou igual a 0 e, se for, já retorna False, porque nenhuma potência de 3 pode ser zero ou negativa. Depois, ele vai dividindo o número por 3 enquanto ele for divisível por 3. No final, se depois de todas as divisões o valor de n for exatamente 1, significa que o número original era uma potência de 3; caso contrário, não era.

def isPowerOfThree(self, n: int) -> bool:
    if n <= 0:
        return False

    while n % 3 == 0:
        n //= 3

    return n == 1

    # return n > 0 and 1162261467 % n == 0

n = 27
print(isPowerOfThree(None, n))