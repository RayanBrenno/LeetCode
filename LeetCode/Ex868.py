# A função percorre o número olhando bit por bit da direita para a esquerda usando deslocamento (n >>= 1). A variável ans guarda a maior distância encontrada entre dois bits 1, count conta a distância atual e find indica se já apareceu o primeiro 1. Cada vez que o bit atual é 1 (n & 1 == 1), ele atualiza a resposta com o maior valor entre o que já tinha e a distância acumulada, depois reinicia o contador para 1 e marca que já encontrou um 1. Se o bit for 0 e já tiver encontrado um 1 antes, ele só incrementa o contador, aumentando a distância. No final, retorna a maior distância entre dois bits 1 consecutivos no número.

def binaryGap(self, n: int) -> int:
    ans = 0
    count = 0
    find = False
    while n > 0:
        if n & 1 == 1:
            ans = max(ans, count)
            count = 1
            find = True
        elif find:
            count += 1

        n >>= 1

    return ans


n = 22
print(binaryGap(None, n))
