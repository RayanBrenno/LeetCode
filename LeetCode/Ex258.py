def addDigits(num):

    while not 0 <= num <= 9:
        num = sum(int(x) for x in str(num))
        print(num)
    return num


num = 38
print(addDigits(num))

print(38%9)
