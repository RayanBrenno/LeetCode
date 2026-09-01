# A função separa a sequência de cores pelos caracteres B e A para identificar grupos consecutivos de A e B com pelo menos 3 elementos. Para cada grupo válido, soma len(x) - 2, representando a quantidade de movimentos possíveis para aquela sequência. Os movimentos de A são somados e os de B subtraídos; no final, retorna True se a quantidade de movimentos de A for maior que a de B, indicando que Alice vence.

def winnerOfGame(self, colors: str) -> bool:
    
    ans = sum(len(x) - 2 for x in colors.split("B") if len(x) >= 3)
    ans -= sum(len(x) - 2 for x in colors.split("A") if len(x) >= 3)

    return ans > 0

    # ans = 0
    # for x in range(1, len(colors) - 1):
    #     aux = colors[x-1:x+2]
    #     ans += 1 if aux == "AAA" else 0
    #     ans -= 1 if aux == "BBB" else 0

    # return ans > 0
    
    
colors = "AAABABB"
print(winnerOfGame(None, colors))  # Output: True