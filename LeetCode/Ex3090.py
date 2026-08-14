# A solução usa Sliding Window com um contador para garantir que nenhum caractere apareça mais de duas vezes na janela atual. Percorremos a string com x, adicionando cada caractere ao counter; quando a frequência do caractere atual passa de 2, movemos o início da janela (start) para frente, removendo os caracteres até que a condição seja válida novamente. A cada iteração, calculamos o tamanho da janela (x - start) e atualizamos ans com o maior valor encontrado.

from collections import defaultdict

def maximumLengthSubstring(self, s: str) -> int:
    ans = 0
    start = -1
    counter = defaultdict(int)
    for x in range(len(s)):
        counter[s[x]] += 1
        while counter[s[x]] > 2:
            start += 1
            counter[s[start]] -= 1
        ans = max(ans, x-start)

    return ans


s = "abcabcabc"
print(maximumLengthSubstring(None, s))