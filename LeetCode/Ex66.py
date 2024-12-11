def plusOne(digits):
    digits = digits[::-1]
    for x in range(len(digits)):
        if digits[x] == 9:
            if x == len(digits) - 1:
                digits[x] = 0
                digits.append(1)
            else: digits[x] = 0
        else:
            digits[x] = digits[x] + 1
            break

    return digits[::-1]

digits = [9]
print(plusOne(digits))

