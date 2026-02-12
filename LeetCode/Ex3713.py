# O algoritmo percorre todas as substrings possíveis começando em cada índice i, e para cada uma vai expandindo o final j, contando quantas vezes cada caractere aparece usando um dicionário. A cada novo caractere, ele atualiza a frequência e verifica se a substring atual é balanceada. O if len(set(count.values())) == 1 funciona pegando todas as quantidades de ocorrência dos caracteres, transformando em um conjunto e verificando se só existe um único valor diferente; se o tamanho do conjunto for 1, significa que todos os caracteres aparecem a mesma quantidade de vezes. Quando isso acontece, ele atualiza o resultado com o maior tamanho encontrado até aquele momento.

from collections import defaultdict

def longestBalanced(self, s: str) -> int:
    n = len(s)
    ans = 0
    for i in range(n):
        count = defaultdict(int)
        for j in range(i, n):
            count[s[j]] += 1
            if len(set(count.values())) == 1:
                ans = max(ans, j - i + 1)
    return ans

s = "aabbcc"
print(longestBalanced(None, s))  # Example usage
