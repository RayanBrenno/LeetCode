# A função começa considerando 1 como divisor, já que todo número maior que 1 possui 1 como divisor. Depois, percorre apenas os números até a raiz quadrada de n, verificando quais dividem n sem resto. Quando encontra um divisor x, soma tanto x quanto seu divisor correspondente n // x, evitando repetir o valor quando os dois são iguais. No final, compara a soma dos divisores com n e retorna True caso sejam iguais, indicando que o número é perfeito, ou False caso contrário.

def checkPerfectNumber(self, num: int) -> bool:
    if num <= 1:
        return False

    ans = 1

    for x in range(2, int(num ** 0.5) + 1):
        if num % x == 0:
            ans += x
            if x != num // x:
                ans += num // x

    return ans == num


num = 28
print(checkPerfectNumber(None, num))  # Output: True