# Esse exercício percorre todos os pares possíveis de valores x e y entre 1 e n e calcula o valor c que poderia formar um trio pitagórico. Em vez de testar todos os c, ele calcula diretamente a raiz de x² + y² e verifica se é um número inteiro e menor ou igual a n. Sempre que a condição é satisfeita, conta um triplo válido, e o total acumulado é a resposta.
 
def countTriples(self, n: int) -> int:
    ans = 0
    for x in range(1, n+1):
        for y in range(1, n+1):
            c = int((x**2 + y**2 + 1)**0.5)
            if c <= n and c**2 == x**2 + y**2:
                ans += 1
    return ans

n = 5
print(countTriples(None, n))  # Output: 2