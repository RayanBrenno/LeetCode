# A ideia é calcular a sequência de Tribonacci, que é parecida com Fibonacci, mas em vez de somar apenas dois termos, soma três: cada valor é a soma dos três anteriores. Começamos com os casos base (T0 = 0, T1 = 1, T2 = 1) e, a partir daí, vamos iterando até n, atualizando três variáveis (a, b, c) que representam os últimos valores da sequência. Em cada passo, calculamos o próximo como a + b + c e avançamos essas variáveis. No final, c contém o valor de Tn.

def tribonacci(self, n: int) -> int:

    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    x1, x2, x3 = 0, 1, 1

    for _ in range(3, n + 1):
        x1, x2, x3 = x2, x3, x1 + x2 + x3

    return x3


n = 25
print(tribonacci(None, n))