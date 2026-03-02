# Esse código constrói o número formado pela concatenação dos valores de 1 até n em binário. Ele percorre os números de 1 até n, e sempre que encontra uma potência de 2 aumenta a variável bits, pois isso significa que a quantidade de bits necessários para representar os números cresceu. A cada passo, ele desloca o resultado atual para a esquerda (<< bits) para abrir espaço e usa | i para adicionar o número atual no final da sequência binária. Para evitar estouro de valor, aplica módulo 10⁹ + 7 a cada iteração. No final, retorna o valor da concatenação binária calculada.


def concatenatedBinary(self, n: int) -> int:
    MOD = 10**9 + 7
    ans = 0
    count = 0

    for i in range(1, n+1):
        if i & (i-1) == 0:
            count += 1
        ans = ((ans << count) | i) % MOD

    return ans


n = 5
print(concatenatedBinary(None, n))
