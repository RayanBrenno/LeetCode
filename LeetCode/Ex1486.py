#O objetivo é calcular o XOR de uma sequência de números gerada pela fórmula start + 2*i. Começamos com ans = 0 e percorremos i de 0 até n-1. Em cada passo calculamos o valor da sequência (start + 2*i) e aplicamos XOR (^=) com ans, acumulando o resultado. No final, ans contém o XOR de todos os n valores gerados, que são números pares espaçados de 2 em 2 a partir de start.

def xorOperation(self, n: int, start: int) -> int:
    ans = 0
    for i in range(n):
        ans ^= start + 2 * i
    return ans


n = 5
start = 0
print(xorOperation(None, n, start))