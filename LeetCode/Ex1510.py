# A solução utiliza **programação dinâmica** para determinar se o jogador que começa consegue vencer. O vetor `dp` guarda, para cada quantidade de pedras `x`, se essa posição é vencedora (`True`) ou perdedora (`False`). Para cada `x`, testamos todas as possibilidades de remover um número de pedras que seja um quadrado perfeito (`1, 4, 9, ...`). Se existir alguma remoção `k²` que leve para uma posição `dp[x - k²]` que seja perdedora para o próximo jogador, então `dp[x]` é marcada como `True`, pois conseguimos deixar o adversário em uma situação ruim. Caso todas as possibilidades levem a posições vencedoras, `dp[x]` permanece `False`. No final, basta retornar `dp[n]`, indicando se o primeiro jogador possui uma estratégia vencedora para `n` pedras.


def winnerSquareGame(self, n: int) -> bool:
    dp = [False] * (n + 1)

    for x in range(1, n + 1):
        k = 1
        while k * k <= x:
            if not dp[x - k * k]:
                dp[x] = True
                break
    return dp[n]


n = 7
print(winnerSquareGame(None, n))  # Output: False
