# Esse código percorre todas as substrings de tamanho k dentro da string s, usando um set chamado seen para armazenar apenas as diferentes (sem repetição). O laço vai de 0 até len(s) - k + 1, e em cada posição pega o trecho s[i:i+k], adicionando no conjunto. No final, ele verifica se a quantidade de substrings únicas encontradas é igual a 2^k (representado por 1 << k, que é um deslocamento de bits equivalente a 2**k). Se for igual, significa que todas as possíveis combinações binárias de tamanho k aparecem na string; caso contrário, não aparecem todas.

def hasAllCodes(self, s: str, k: int) -> bool:

    ans = set()
    for x in range(len(s)-k+1):
        ans.add(s[x:x+k])

    return len(ans) == 1 << k
    # return len(ans) == 2 ** k


s = "00110110"
k = 2
print(hasAllCodes(None, s, k))



test = {"Rayan": [("10", "sf", 1)],
        "Bruna": [("20", "sf", 2)],
        "Maria": [("30", "sf", 3)]}


for t, c, index in test["Rayan"]:
    print(t, c, index)
