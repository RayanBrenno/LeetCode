# A lógica fica: length testa os possíveis tamanhos de substring começando em k; end percorre todas as substrings daquele tamanho; substring.count("1") == k verifica se ela é bonita; entre as bonitas, ans guarda a lexicograficamente menor. Assim que ans existe, retornamos porque estamos testando os tamanhos em ordem crescente, então aquele é necessariamente o menor tamanho possível.

def shortestBeautifulSubstring(self, s: str, k: int) -> str:
    n = len(s)

    for length in range(k, n + 1):
        ans = ""

        for end in range(length, n + 1):
            substring = s[end - length:end]

            if substring.count("1") == k and (not ans or substring < ans):
                ans = substring

        if ans:
            return ans

    return ""


s = "111000111"
k = 3
print(shortestBeautifulSubstring(None, s, k))  # Output: "111"