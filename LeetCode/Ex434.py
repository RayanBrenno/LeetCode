# A função verifica primeiro se a string está vazia, retornando 0 nesse caso. Caso contrário, utiliza split() para separar a string em palavras, ignorando espaços extras, e retorna a quantidade de elementos resultantes, que corresponde ao número de segmentos presentes na string.

def countSegments(self, s: str) -> int:
    if "" == s:
        return 0
    return len(s.split())


s = "Hello, my name is John"
print(countSegments(None, s))  # Output: 5