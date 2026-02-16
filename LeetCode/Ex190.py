# Ele percorre os 32 bits do número, e a cada passo pega o último bit com n & 1, move res uma posição pra esquerda (res << 1) para abrir espaço e usa | aux para colocar esse bit no final. Depois desloca n pra direita (n >>= 1) para remover o bit já usado. No final das 32 iterações, res contém todos os bits de n na ordem invertida.

def reverseBits(n: int) -> int:
    res = 0

    for _ in range(32):
        aux = n & 1
        res = (res << 1) | aux
        n >>= 1

    return res

n = 00000010100101000001111010011100
print(reverseBits(n))