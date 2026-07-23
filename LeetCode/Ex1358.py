# O algoritmo percorre a string apenas uma vez, mantendo em last_pos a última posição em que cada caractere ('a', 'b' e 'c') foi encontrado. A cada nova posição, ele atualiza a ocorrência da letra atual e calcula quantas substrings válidas terminam naquele índice. Para isso, utiliza min(last_pos), que representa a ocorrência mais antiga entre as últimas aparições das três letras. Qualquer substring que comece entre o índice 0 e essa menor posição conterá obrigatoriamente um 'a', um 'b' e um 'c', totalizando min(last_pos) + 1 possibilidades. Caso alguma letra ainda não tenha aparecido, seu valor em last_pos permanece -1, fazendo com que nenhuma substring seja contabilizada naquele momento. Dessa forma, a resposta é obtida somando as contribuições de cada posição em tempo O(n).

def numberOfSubstrings(self, s: str) -> int:
    prev = [-1] * 3
    ans = 0

    for x in range(len(s)):
        prev[ord(s[x]) - ord("a")] = x
        ans += min(prev) + 1

    return ans


s = "abcabc"
print(numberOfSubstrings(None, s))