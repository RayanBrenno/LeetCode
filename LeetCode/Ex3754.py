# A solução percorre os dígitos de n da esquerda para a direita, ignorando os zeros. Para cada dígito diferente de zero, ela reconstrói o número x usando ans = ans * 10 + int(x), o que adiciona o novo dígito ao final do número mantendo a ordem original. Ao mesmo tempo, acumula a soma desses dígitos em sumN. No final, retorna o produto entre o número formado (ans) e a soma de seus dígitos (sumN).

def sumAndMultiply(self, n: int) -> int:
        sumN = 0
        ans = 0
        for x in str(n):
            if x != "0":
                ans = ans * 10 + int(x)
                sumN += int(x)
        return ans * sumN
    

n = 10203004
print(sumAndMultiply(None, n))