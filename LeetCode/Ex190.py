def reverseBits(n: int) -> int:
    res = 0

    for _ in range(32):
        aux = n & 1
        res = (res << 1) | aux
        n >>= 1

    return res

n = 00000010100101000001111010011100
print(reverseBits(n))