# A solução percorre todos os dígitos do número uma única vez, extraindo cada um com % 10 e removendo-o com divisão inteira (// 10). Durante esse processo, mantém as duas maiores cifras encontradas nas variáveis first e second: se o dígito atual for maior que first, ambos são atualizados; caso contrário, se for apenas maior que second, apenas second é alterado. Ao final, basta retornar o produto entre os dois maiores dígitos, evitando a necessidade de armazenar ou ordenar todos os dígitos do número, o que torna a solução simples e eficiente.

def maxProduct(self, n: int) -> int:
    first, second = 0, 0
    while n:
        x = n % 10
        if x > first:
            first, second = x, first
        elif x > second:
            second = x
        n //= 10
    return first * second


n = 234
print(maxProduct(None, n))
