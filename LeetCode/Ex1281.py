# O código converte o número em uma lista de dígitos, calcula a soma de todos eles utilizando sum() e percorre a lista novamente para multiplicá-los, armazenando o resultado em aux2. Por fim, retorna a diferença entre o produto e a soma dos dígitos.

def subtractProductAndSum(self, n: int) -> int:
    # total = 0
    # product = 1
    # while n > 0:
    #     aux = n % 10
    #     total += aux
    #     product *= aux
    #     n //= 10

    # return product - total

    arr = list(str(n))
    aux1 = sum(int(x) for x in arr)
    aux2 = 1
    for x in arr:
        aux2 *= int(x)
    return aux2 - aux1


n = 234
print(subtractProductAndSum(None, n))
