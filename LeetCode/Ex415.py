def addStrings(num1: str, num2: str) -> str:

    maxLength = max(len(num1), len(num2))
    num1 = num1.zfill(maxLength)
    num2 = num2.zfill(maxLength)
    carry = 0
    res = []
    for x, y in zip(reversed(num1), reversed(num2)):
        value1 = ord(x) - ord('0')
        value2 = ord(y) - ord('0')

        total = value1 + value2 + carry
        carry = total // 10
        res.append(str(total % 10))
    if carry == 1:
        res.append(str(carry))
    return ''.join(res[::-1])


num1 = "123"
num2 = "456"
print(addStrings(num1, num2))
