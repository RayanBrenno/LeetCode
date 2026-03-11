# A solução inverte a ordem das palavras de uma string. Primeiro usamos split() para separar a frase em uma lista de palavras, automaticamente removendo espaços extras. Depois usamos [::-1] para inverter a lista. Por fim, usamos " ".join() para juntar as palavras novamente em uma única string separada por espaços. O resultado é a frase original com as palavras em ordem reversa.

def reverseWords(self, s: str) -> str:
    words = s.split()
    return " ".join(words[::-1])


s = "  hello world!  "
print(reverseWords(s))
    