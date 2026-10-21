# A ideia principal é usar zip() para percorrer as duas palavras simultaneamente, concatenando cada par de caracteres na string ans de forma alternada. Como o zip() para quando a menor palavra termina, usamos slicing para adicionar o restante de ambas as palavras, sendo que a palavra menor não terá nenhum caractere restante.

def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""

        for x, y in zip(word1, word2):
            ans += x + y

        return ans + word1[len(word2):] + word2[len(word1):]
    
    

word1 = "abc"
word2 = "pqr"
print(mergeAlternately(word1, word2))  