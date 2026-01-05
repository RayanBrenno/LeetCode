def getKth(lo: int, hi: int, k: int) -> int:
    auxGeral = {}
    def calcPower(x):
        if x in auxGeral: 
            return auxGeral[x]
        if x == 1:
            return 0
        if x % 2 == 0:
            n = x//2
        else:
            n = 3 * x + 1
        
        auxGeral[x] = 1 + calcPower(n)
        return auxGeral[x]

    powers = [[num, calcPower(num)] for num in range(lo, hi+1)]
    powers = sorted(powers, key=lambda x: x[1])
    return powers[k-1][0]

    """
    
    def calcPower(x, power):
         if x == 1: return power
            
        if x % 2 == 0:
            return calcPower(x/2, power+1)
        else:
            return calcPower((3*x)+1, power+1)

    powers = [[num, calcPower(num, 0)] for num in range(lo, hi+1)]
    powers = sorted(powers, key=lambda x: x[1])
    return powers[k-1][0]
    """

    
    """
    res = [[num, 0] for num in range(lo, hi+1)]
    pointer, n = 0, len(res)
    aux = res[pointer][0]
    while pointer < n:
        if aux == 1:
            pointer += 1
            aux = res[pointer][0] if pointer < n else 0
            continue

        aux = aux/2 if aux % 2 == 0 else 3*aux + 1
        res[pointer][1] += 1
    res = sorted(res, key=lambda x: x[1])

    return res[k-1][0]
    """


lo = 7
hi = 11
k = 4
print(getKth(lo, hi, k))
