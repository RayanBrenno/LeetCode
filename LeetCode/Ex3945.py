# O algoritmo calcula a soma dos dígitos de n utilizando operações matemáticas. A cada iteração, n % 10 obtém o último dígito, que é somado em ans, enquanto n //= 10 remove esse dígito. O processo se repete até que n seja zero, retornando a soma total dos seus dígitos.

def digitFrequencyScore(self, n: int) -> int:
    # count = defaultdict(int)
    # for x in str(n):
    #     count[x] += 1
    # return sum(int(x) * y for x, y in count.items())

    ans = 0

    while n > 0:
        ans += n % 10
        n //= 10

    return ans


n = 12345
print(digitFrequencyScore(None, n))