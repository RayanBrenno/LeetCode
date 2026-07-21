# A ideia é utilizar uma Sliding Window de tamanho k, onde cada janela representa um possível trecho que pode ser transformado em k blocos pretos consecutivos. Inicialmente, contamos quantos blocos brancos ('W') existem na primeira janela, pois essa quantidade corresponde ao número de operações necessárias para torná-la completamente preta. Em seguida, deslizamos a janela uma posição por vez, removendo da contagem o caractere que saiu da janela caso seja 'W' e adicionando o novo caractere que entrou caso também seja 'W'. A cada deslocamento, atualizamos a resposta com o menor número de blocos brancos encontrado entre todas as janelas, já que essa será a menor quantidade de recolorações necessárias para obter pelo menos um trecho com k blocos pretos consecutivos.

def minimumRecolors(self, blocks: str, k: int) -> int:
    white = blocks[:k].count('W')
    ans = white

    for x in range(k, len(blocks)):
        if blocks[x - k] == 'W':
            white -= 1
        if blocks[x] == 'W':
            white += 1
        ans = min(ans, white)

    return ans


blocks = "WBBWWBBWBW"
k = 7
print(minimumRecolors(None, blocks, k))  # Output: 3