# Esse exercício constrói iterativamente a sequência binária definida pela regra Sn = S(n-1) + "1" + reverse(invert(S(n-1))), começando de "0", e o objetivo é retornar o k-ésimo bit da sequência no nível n. O algoritmo começa com sequence = "0" e, a cada iteração, cria a próxima versão invertendo todos os bits da sequência atual (0↔1), depois aplicando reverse, adicionando "1" no meio e concatenando tudo. O loop para antecipadamente quando o tamanho já é suficiente para alcançar a posição k, evitando crescer desnecessariamente. No final, retorna sequence[k-1] porque a string é indexada a partir de 0. A lógica funciona, mas tem custo exponencial no pior caso, já que o tamanho da sequência cresce como 2^n - 1

def findKthBit(self, n: int, k: int) -> str:
    sequence = "0"
    for x in range(n):
        if k <= len(sequence):
            break
        inverted = ["1" if x == "0" else "0" for x in sequence]
        sequence = sequence + "1" + "".join(inverted)[::-1]
    return sequence[k-1]


n = 3
k = 1
print(findKthBit(None, n, k))