# Esse código valida a string usando uma abordagem baseada em posições, não só contagem. Ele percorre a string guardando os índices dos "(" e dos "*" em duas listas separadas. Quando encontra um ")", tenta primeiro fechar com o "(" mais recente; se não tiver, usa um * como substituto. Se não houver nenhum dos dois, a string já é inválida. Depois do loop, podem sobrar "(" abertos, então o algoritmo tenta fechá-los usando os * restantes. Porém, isso só é válido se o * estiver depois do "(", o que é verificado comparando os índices: se um "(" aparece depois de um *, não dá pra fechá-lo, então retorna False. No final, a string só é válida se todos os "(" forem corretamente balanceados, ou seja, se não sobrar nenhum na lista.

def checkValidString(self, s: str) -> bool:
    open_par = []
    asterisks = []

    for index, char in enumerate(s):
        if char == "(":
            open_par.append(index)

        elif char == "*":
            asterisks.append(index)

        else:
            if open_par:
                open_par.pop()
            elif asterisks:
                asterisks.pop()
            else:
                return False

    while open_par and asterisks:
        if open_par.pop() > asterisks.pop():
            return False

    return True if len(open_par) == 0 else False


s = "(*))"
print(checkValidString(None, s))