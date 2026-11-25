# A solução percorre a string considerando cada posição como início de um possível substring e avança enquanto encontrar apenas vogais, utilizando um conjunto (set) para armazenar as vogais distintas encontradas. Sempre que o conjunto contém as cinco vogais, incrementa ans, contabilizando um novo substring válido. Caso encontre uma consoante, interrompe a busca a partir daquela posição.

def countVowelSubstrings(self, word: str) -> int:
    vowels = set("aeiou")
    ans = 0

    for x in range(len(word)):
        seen = set()

        for y in range(x, len(word)):
            if word[y] not in vowels:
                break

            seen.add(word[y])

            if len(seen) == 5:
                ans += 1

    return ans


word = "aeiouu"
print(countVowelSubstrings(None, word))
