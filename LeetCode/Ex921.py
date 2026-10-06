# A implementação percorre a string contando os parênteses abertos e, ao encontrar um `)`, verifica se existe algum `(` disponível para formar um par; caso exista, reduz `open_par`, caso contrário, conta esse fechamento como inválido em `close_par`. No final, a soma de `close_par` com `open_par` representa a quantidade mínima de parênteses que precisam ser adicionados para tornar a string válida.


def minAddToMakeValid(self, s: str) -> int:
    open_par = 0
    close_par = 0

    for x in s:
        if x == "(":
            open_par += 1
        else:
            if open_par > 0:
                open_par -= 1
            else:
                close_par += 1

    return close_par + open_par


s = "())"
print(minAddToMakeValid(None, s))
