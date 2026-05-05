# Percorremos todos os números de 1 até n e convertemos cada um para string para facilitar a análise dos dígitos. Se o número contiver algum dígito inválido para rotação (3, 4, 7), ele é ignorado. Caso contrário, verificamos se possui ao menos um dígito que muda após a rotação (2, 5, 6, 9); se tiver, incrementamos ans, pois esse número é considerado good.

def rotatedDigits(self, n: int) -> int:
    ans = 0

    for x in range(1, n + 1):
        num = str(x)
        if '3' in num or '4' in num or '7' in num:
            continue
        if '2' in num or '5' in num or '6' in num or '9' in num:
            ans += 1

    return ans


# ans = 0
# for x in range(1, n+1):
#     num = str(x)
#     if any(digit in num for digit in "347"):
#         continue
#     if any(digit in num for digit in "2569"):
#         ans += 1

# return ans

n = 10
print(rotatedDigits(None, n))
