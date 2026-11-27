# A implementação gera a sequência de Fibonacci até alcançar ou ultrapassar k e, em seguida, percorre os números do maior para o menor, subtraindo de k sempre que possível e incrementando ans a cada subtração. Dessa forma, utiliza a estratégia gulosa para encontrar a menor quantidade de números de Fibonacci cuja soma seja igual a k.

def findMinFibonacciNumbers(self, k: int) -> int:
    if k < 2:
        return k

    fin = [1, 1]
    ans = 0

    while k > fin[-1]:
        fin.append(fin[-1] + fin[-2])

    n = len(fin) - 1
    while n >= 0:
        if k >= fin[n]:
            ans += 1
            k -= fin[n]
        n -= 1

    return ans


k = 7
print(findMinFibonacciNumbers(None, k))
