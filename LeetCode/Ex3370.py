def smallestNumber(self, n: int) -> int:
    aux = 2
    while aux <= n:
        aux *= 2
    return aux-1


n = 5
print(smallestNumber(None, n))