# A implementação percorre a string mantendo em `openIndices` as posições onde cada parêntese de abertura foi encontrado. Ao encontrar um `)`, recupera a última posição aberta, remove-a da pilha e inverte a parte de `ans` a partir daquele índice, garantindo que os parênteses internos sejam processados antes dos externos. Os parênteses não são adicionados ao resultado e, ao final, `ans` é convertido em uma string com `join`.


def reverseParentheses(self, s: str) -> str:
    ans = []
    openIndices = []

    for x in s:
        if x == "(":
            openIndices.append(len(ans))
        elif x == ")":
            aux = openIndices[-1]
            openIndices.pop()
            ans[aux:] = ans[aux:][::-1]
        else:
            ans.append(x)

    return "".join(ans)


s = "(ed(et(oc))el)"
print(reverseParentheses(None, s))  # Output: "leetcode"
