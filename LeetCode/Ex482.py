# A solução começa removendo todos os hífens da string e convertendo todas as letras para maiúsculas. Em seguida, calcula o tamanho do primeiro grupo usando o resto da divisão do tamanho da string por k, já que apenas esse grupo pode ter menos de k caracteres. Se esse grupo existir, ele é adicionado à resposta. Depois, percorre o restante da string em blocos de tamanho k, adicionando cada um à lista de grupos. Por fim, todos os grupos são unidos com hífens utilizando "-".join(), produzindo a chave de licença no formato desejado.

def licenseKeyFormatting(self, s: str, k: int) -> str:
    s = s.replace("-", "").upper()
    ans = []
    first = len(s) % k

    if first:
        ans.append(s[:first])

    for x in range(first, len(s), k):
        ans.append(s[x:x+k])

    return "-".join(ans)


s = "5F3Z-2e-9-w"
k = 4
print(licenseKeyFormatting(None, s, k))