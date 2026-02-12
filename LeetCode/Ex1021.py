# A gente percorre a string contando a profundidade dos parênteses. Sempre que encontramos um ( e o contador já é maior que 0, adicionamos ele ao resultado, pois não é o mais externo. Para ), primeiro diminuímos o contador e só adicionamos se ainda for maior que 0. Assim removemos automaticamente os parênteses externos de cada bloco primitivo.

def removeOuterParentheses(self, s: str) -> str:
    ans = []
    aux = 0

    for x in s:
        if x == "(":
            if aux > 0:
                ans.append(x)
            aux += 1
        else:
            aux -= 1
            if aux > 0:
                ans.append(x)

    return "".join(ans)


s = "(()())(())"
print(removeOuterParentheses(None, s))  