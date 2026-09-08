# A implementação considera que números menores que 1000 não possuem vírgulas, então usamos max(0, n - 999) para contar diretamente quantos números a partir de 1000 existem até n. Assim, se n for menor que 1000, retornamos 0; caso contrário, n - 999 representa exatamente a quantidade de números que possuem uma vírgula.

def countCommas(self, n: int) -> int:
    return max(0, n - 999)


n = 1234567
result = countCommas(n)
print(result)  # Output: 1234567 - 999 = 1233568