# Percorremos a string convertida em lista para poder modificar seus caracteres. Sempre que encontramos um '?', testamos apenas as letras 'a', 'b' e 'c' e escolhemos a primeira que seja diferente dos caracteres vizinhos (à esquerda e à direita, quando existirem). Como no máximo duas letras podem estar proibidas, sempre haverá uma opção válida entre essas três. Ao final, juntamos a lista novamente em uma string e retornamos o resultado.

def modifyString(self, s: str) -> str:
    s = list(s)

    for i in range(len(s)):
        if s[i] == "?":
            for c in "abc":
                if i > 0 and s[i - 1] == c:
                    continue
                if i < len(s) - 1 and s[i + 1] == c:
                    continue
                s[i] = c
                break

    return "".join(s)


s = "?zs"
print(modifyString(None, s))