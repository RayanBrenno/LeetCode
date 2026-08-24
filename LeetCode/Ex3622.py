# A implementação percorre cada dígito de n convertendo o número para string, acumulando sua soma em sum1 e seu produto em product1. Ao final, verifica se n é divisível pela soma desses dois valores usando o operador %, retornando True caso o resto seja 0 e False caso contrário.

def checkDivisibility(self, n: int) -> bool:
    product1 = 1
    sum1 = 0
    for x in str(n):
        product1 *= int(x)
        sum1 += int(x)

    return True if n % (sum1 + product1) == 0 else False


n = 12
print(checkDivisibility(None, n))