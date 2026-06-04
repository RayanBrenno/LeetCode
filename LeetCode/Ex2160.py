# Transforme o número em uma lista de dígitos, ordene em ordem crescente e distribua os dígitos alternadamente entre duas strings (new1 e new2). Dessa forma, os menores dígitos ficam nas casas mais significativas dos dois números, minimizando a soma final. Ao final, converta as strings para inteiro e retorne a soma.

def minimumSum(self, num: int) -> int:
    aux = sorted(list(str(num)))
    new1, new2 = "", ""

    for x in range(0, 4, 2):
        new1 += aux[x]
        new2 += aux[x + 1]

    return int(new1) + int(new2)


num = 4009
print(minimumSum(None, num))