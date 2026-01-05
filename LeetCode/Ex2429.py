def minimizeXor(num1: int, num2: int) -> int:

    def countingBits(n):
        res = 0
        while n > 0:
            res += 1 & n
            n = n >> 1
        return res

    x = num1
    count1, count2 = countingBits(num1), countingBits(num2)
    i = 0

    while count1 > count2:
        if x & (1 << i):
            count1 -= 1
            x = x ^ (1 << i)
        i += 1

    while count1 < count2:
        if x & (1 << i) == 0:
            count1 += 1
            x = x | (1 << i)
        i += 1

    return x


num1 = 13000
num2 = 14536
print(minimizeXor(num1, num2))
