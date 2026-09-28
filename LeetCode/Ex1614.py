# A implementação percorre a string mantendo `aux` como a profundidade atual dos parênteses: incrementa ao encontrar `(` e decrementa ao encontrar `)`. A cada posição, atualiza `ans` com a maior profundidade encontrada usando `max`, retornando ao final o maior nível de aninhamento da expressão.


def maxDepth(self, s: str) -> int:
    ans, aux = 0, 0
    for x in s:
        if x == '(':
            aux += 1
        elif x == ')':
            aux -= 1
        ans = max(ans, aux)
    return ans


s = "1+(2*3)/(2-1)"
print(maxDepth(s))  # Output: 1
