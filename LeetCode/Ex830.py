# Percorremos a string identificando quando um caractere diferente aparece, indicando o fim de um grupo. Se o tamanho do grupo for pelo menos 3, adicionamos seu intervalo à resposta. Ao final, verificamos também o último grupo, já que ele pode terminar junto com a string.

def largeGroupPositions(self, s: str) -> list[list[int]]:
    ans = []
    start = 0

    for x in range(1, len(s)):
        if s[x] != s[start]:
            if x - start >= 3:
                ans.append([start, x - 1])
            start = x

    if len(s) - start >= 3:
        ans.append([start, len(s) - 1])

    return ans


s = "abbxxxxzzy"
print(largeGroupPositions(None, s))  # Output: [[3, 6]]
