# A solução retorna diretamente n porque o MDC entre a soma dos primeiros n números ímpares e a soma dos primeiros n números pares sempre simplifica para n: a soma dos ímpares é n², a soma dos pares é n(n+1), então gcd(n², n(n+1)) = n * gcd(n, n+1) = n, já que números consecutivos sempre têm MDC igual a 1.

def gcdOfOddEvenSums(self, n: int) -> int:
    return n


n = 10
print(gcdOfOddEvenSums(None, n))