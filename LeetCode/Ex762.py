# Essa função percorre todos os números entre left e right, e verifica cada um individualmente. Para cada número, ela converte o valor para sua representação binária usando bin(x) e conta quantos bits 1 aparecem nessa representação com .count('1'). Depois disso, ela verifica se essa quantidade de bits 1 está dentro de uma lista pré-definida de números primos. Se estiver, significa que aquele número atende à condição do problema, então o contador res é incrementado. No final do processo, a função retorna quantos números dentro do intervalo possuem uma quantidade de bits 1 que é um número primo.

def countPrimeSetBits(left: int, right: int) -> int:
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    res = 0

    for x in range(left, right+1):
        bits = bin(x).count('1')
        if bits in primes:
            res += 1
    return res


left = 6
right = 10
print(countPrimeSetBits(left, right))