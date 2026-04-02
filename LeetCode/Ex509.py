# A ideia é calcular o valor de Fibonacci de forma iterativa, evitando recursão. Começamos tratando os casos base (n = 0 e n = 1). Depois, usamos duas variáveis (x0 e x1) para representar os dois últimos valores da sequência. A cada iteração, atualizamos essas variáveis fazendo x0, x1 = x1, x0 + x1, ou seja, avançamos na sequência somando os dois anteriores. No final, x1 contém o valor de fib(n).

def fib(self, n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1

    x0, x1 = 0, 1

    for _ in range(2, n+1):
        x0, x1 = x1, x0 + x1

    return x1


n = 25
print(fib(None, n))