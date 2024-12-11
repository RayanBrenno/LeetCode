def isUgly(n):
    if n == 0:
        return False
    for x in 2, 3, 5:
        while n % x == 0:
            n /= x
    return n == 1


n = 14
print(isUgly(n))
