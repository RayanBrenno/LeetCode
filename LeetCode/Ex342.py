# Esse código verifica se um número é potência de 4. Primeiro ele checa se n é menor ou igual a 0 e, se for, já retorna False, porque potências de 4 são sempre positivas. Depois, enquanto o número for divisível por 4, ele vai dividindo por 4. No final, se depois de todas as divisões o valor de n for exatamente 1, significa que o número original era uma potência de 4; se sobrar qualquer outro valor, então não era.

def isPowerOfFour(self, n: int) -> bool:
    if n <= 0:
        return False

    while n % 4 == 0:
        n //= 4

    return n == 1

n = 16
print(isPowerOfFour(None, n))