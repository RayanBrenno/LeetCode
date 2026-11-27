# A implementação simula as rodadas de Alice e Bob, começando com a remoção de 10 pedras e diminuindo a quantidade em 1 a cada turno. Enquanto houver pedras suficientes, subtrai a quantidade correspondente e alterna o jogador usando XOR para controlar os turnos. No final, retorna True se Alice foi a última a jogar.

def canAliceWin(self, n: int) -> bool:
    aux, count = 10, 0

    while n >= aux:
        n -= aux
        count ^= 1
        aux -= 1

    return bool(count & 1)


n = 10
print(canAliceWin(None, n))
