# A ideia é contar quantas permutações de 1 até n respeitam que números primos só fiquem em posições primas. Primeiro, usamos a função prime para descobrir quantos primos existem até n, armazenando isso em aux. Como existem exatamente aux posições primas, podemos organizar esses números primos nessas posições de aux! formas (calculado em factorial_aux). Já os números não-primos (n - aux) ocupam o restante das posições e podem ser organizados de (n - aux)! formas (calculado em factorial_dif). No final, multiplicamos factorial_aux por factorial_dif e aplicamos o módulo 10^9 + 7 para obter o resultado.

def numPrimeArrangements(self, n: int) -> int:
    MOD = 10**9 + 7

    def prime(num):
        if num < 2:
            return False
        for y in range(2, int(num**0.5) + 1):
            if num % y == 0:
                return False
        return True

    aux = sum(1 for x in range(1, n + 1) if prime(x))

    factorial_aux = 1
    for x in range(1, aux + 1):
        factorial_aux = (factorial_aux * x) % MOD

    factorial_dif = 1
    for x in range(1, n - aux + 1):
        factorial_dif = (factorial_dif * x) % MOD

    return (factorial_aux * factorial_dif) % MOD


n = 100
print(numPrimeArrangements(None, n))