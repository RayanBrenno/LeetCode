# A implementação conta a quantidade de fatores 5 presentes em n!, já que cada zero no final surge da combinação de um fator 2 com um fator 5, e os fatores 2 estão sempre em maior quantidade. A cada iteração, n é dividido por 5 para contar os múltiplos de 5, depois por 25, 125 e assim por diante, contabilizando também os fatores 5 extras presentes nesses números. A soma dessas divisões representa diretamente a quantidade de zeros no final de n!.

def trailingZeroes(self, n: int) -> int:
        ans = 0

        while n > 0:
            n //= 5
            ans += n

        return ans


n = 100
print(trailingZeroes(n))  # Saída: 24