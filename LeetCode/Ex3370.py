# Começa com uma potência de 2 (aux = 2) e vai dobrando até passar de n, quando isso acontece subtrai 1, porque um número do tipo 2^k - 1 tem todos os bits iguais a 1 e é o menor número maior ou igual a n com essa propriedad

def smallestNumber(self, n: int) -> int:
    aux = 2
    while aux <= n:
        aux *= 2
    return aux-1


n = 5
print(smallestNumber(None, n))