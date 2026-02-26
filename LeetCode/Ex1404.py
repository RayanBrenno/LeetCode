# Essa versão transforma a string em lista e simula o processo no binário mesmo. Enquanto o número não virar só "1", ela faz: se terminar com "0", remove o último bit (divide por 2) e soma um passo; se terminar com "1", simula um +1 propagando o carry da direita pra esquerda (trocando 1 por 0 até achar um 0 pra virar 1, ou adicionando 1 no começo se for tudo 1). Vai contando cada operação até reduzir para 1.

def numSteps(self, s: str) -> int:
    ans = 0
    arr = list(s)

    while len(arr) > 1:
        if arr[-1] == "0":
            ans += 1
            arr.pop()

        else:
            ans += 1
            x = len(arr) - 1
            while x >= 0 and arr[x] == "1":
                arr[x] = "0"
                x -= 1
            if x >= 0:
                arr[x] = "1"
            else:
                arr = ["1"] + arr

    return ans


s = "1101"
print(numSteps(None, s))
