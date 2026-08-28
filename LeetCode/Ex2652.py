# A função percorre todos os números de 1 até n e verifica quais são múltiplos de 3, 5 ou 7 usando o operador %. Quando o número atende a pelo menos uma dessas condições, ele é somado em ans, que no final é retornado como a soma de todos os múltiplos encontrados.

def sumOfMultiples(self, n: int) -> int:
    ans = 0
    for x in range(1, n + 1):
        if x % 3 == 0 or x % 5 == 0 or x % 7 == 0:
            ans += x
    return ans
    # return sum(x for x in range(1, n + 1) if x % 3 == 0 or x % 5 == 0 or x % 7 == 0)


n = 7
print(sumOfMultiples(None, n))  # Output: 21