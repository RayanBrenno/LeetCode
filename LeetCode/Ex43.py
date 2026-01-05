def multiply(num1: str, num2: str) -> str:
    if num1 == '0' or num2 == '0':
        return '0'
    
    def funSum(num1, num2):
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

    res = "0"

    for x in range(len(num2)-1, -1, -1):

        value1 = ord(num2[x]) - ord('0')
        carry = 0
        aux = ["0"] * (len(num2) - 1 - x)

        for y in reversed(num1):
            value2 = ord(y) - ord('0')
            total = value1 * value2 + carry
            carry = total // 10
            aux.append(str(total % 10))

        if carry != 0:
            aux.append(str(carry))

        res = funSum(res, "".join(aux[::-1]))


num1 = "10"
num2 = "0"
print(multiply(num1, num2))
