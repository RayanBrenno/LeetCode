# A implementação percorre a string da esquerda para a direita procurando palíndromos de tamanho k ou k + 1, que são as menores opções possíveis para aproveitar melhor o espaço e maximizar a quantidade de substrings. Quando encontra um palíndromo, incrementa ans e avança x pelo tamanho encontrado, evitando sobreposição; caso não encontre nenhum, avança apenas uma posição para continuar a busca. A verificação do palíndromo é feita comparando o substring com sua versão invertida.

def maxPalindromes(self, s: str, k: int) -> int:
    n = len(s)
    if k == 1:
        return n

    ans, x = 0, 0

    while x <= n - k:
        for y in (k, k+1):
            if x + y <= n and s[x: x + y] == s[x: x + y][::-1]:
                ans += 1
                x += y
                break
        else:
            x += 1
    return ans


s = "abaccdbbd"
k = 3
print(maxPalindromes(s, k))  # Saída: 2