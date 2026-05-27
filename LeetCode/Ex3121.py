# A solução usa dois dicionários: last_lower guarda o último índice de cada letra minúscula, e first_upper guarda o primeiro índice de cada letra maiúscula. Depois, para cada letra minúscula encontrada, verifica se a versão maiúscula existe e se o último lowercase vem antes do primeiro uppercase, incrementando o contador se sim.

def numberOfSpecialChars(self, word: str) -> int:
    last_lower = {}
    first_upper = {}

    for index, char in enumerate(word):
        if char.islower():
            last_lower[char] = index
        else:
            if char not in first_upper:
                first_upper[char] = index

    ans = 0
    for x in last_lower:
        if x.upper() in first_upper and last_lower[x] < first_upper[x.upper()]:
            ans += 1

    return ans


# Exemplo de uso
word = "aAbBcC"
print(numberOfSpecialChars(None, word))  # Saída: 3 (a, b