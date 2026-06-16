# Percorremos a string caractere por caractere, mantendo uma resposta parcial. Se o caractere for uma letra, ele é adicionado ao resultado. Quando encontramos #, duplicamos todo o conteúdo atual; com %, invertimos a ordem dos caracteres; e com *, removemos o último caractere. Ao final, retornamos a string construída após aplicar todas as operações na sequência em que aparecem.

def processStr(self, s: str) -> str:
    ans = ""
    for x in s:
        if x == "#":
            ans += ans
        elif x == "%":
            ans = ans[::-1]
        elif x == "*":
            ans = ans[:-1]
        else:
            ans += x
    return ans


s = "abc#d%*e"
result = processStr(None, s)