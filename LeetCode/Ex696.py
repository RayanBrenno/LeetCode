# Esse código percorre a string contando quantos caracteres iguais aparecem seguidos (curr) e guarda também o tamanho do bloco anterior (prev). Sempre que encontra uma mudança de caractere (de 0 para 1 ou vice-versa), ele soma ao resultado o menor valor entre o bloco atual e o anterior, pois isso representa quantas substrings válidas podem ser formadas com a mesma quantidade de 0s e 1s consecutivos. Depois atualiza prev com o valor de curr e reinicia curr como 1. No final, ainda soma o min(prev, curr) restante para considerar o último grupo, retornando assim o total de substrings binárias válidas.

def countBinarySubstrings(self, s: str) -> int:
    count = 0
    prev = 0
    curr = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            curr += 1
        else:
            count += min(prev, curr)
            prev = curr
            curr = 1

    return count + min(prev, curr)


s = "00110011"
print(countBinarySubstrings(None, s))