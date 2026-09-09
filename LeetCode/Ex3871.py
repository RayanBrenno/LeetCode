# A implementação percorre as casas de milhar, milhão, bilhão etc., contando quantos números a partir de cada potência de 1000 possuem uma vírgula. A cada nível, soma n - aux + 1 ao total e multiplica aux por 1000 para verificar a próxima faixa.

def countCommas(self, n: int) -> int:
    ans, aux = 0, 1000

    while aux <= n:
        ans += n - aux + 1
        aux *= 1000

    return ans


n = 1000000
print(countCommas(n))  # Saída: 1001