# A solução testa todas as possíveis quantidades de doces para a primeira e a segunda criança, variando de 0 até limit. Para cada combinação, calcula automaticamente a quantidade da terceira criança como n - a - b. Se esse valor estiver entre 0 e limit, significa que a distribuição é válida e a resposta é incrementada. Ao final, retorna o total de distribuições possíveis.

def distributeCandies(self, n: int, limit: int) -> int:
    ans = 0

    for a in range(limit + 1):
        for b in range(limit + 1):
            c = n - a - b

            if 0 <= c <= limit:
                ans += 1

    return ans


n = 7
limit = 3
print(distributeCandies(None, n, limit))