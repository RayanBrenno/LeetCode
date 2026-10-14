# A implementação verifica primeiro se a soma desejada é maior que o máximo possível (num * 9), retornando uma string vazia caso não seja possível formar o número. Em seguida, adiciona o dígito 9 enquanto a soma for maior ou igual a 9, subtraindo seu valor a cada iteração para maximizar o score. Se ainda restar algum valor, ele é adicionado como um único dígito e, por fim, zeros são acrescentados até completar a quantidade exata de dígitos. Ao juntar os elementos de ans, retorna o maior número possível que atende às condições do problema.

def maxSumOfSquares(self, num: int, sum: int) -> str:
    if sum > num * 9:
        return ""
    ans = []

    while sum >= 9:
        ans.append("9")
        sum -= 9

    if sum > 0:
        ans.append(str(sum))

    while len(ans) < num:
        ans.append("0")

    return "".join(ans)


num = 3
sum = 20
print(maxSumOfSquares(None, num, sum))
