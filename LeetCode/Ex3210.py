# Calcula k % n para evitar rotações desnecessárias e cria uma nova string percorrendo cada posição x, pegando o caractere que está k posições à frente de forma circular com (x + k) % n. No final, retorna a string rotacionada para a esquerda em k posições.

def getEncryptedString(self, s: str, k: int) -> str:
    ans = ""
    n = len(s)
    k = k % n
    for x in range(n):
        ans += s[(x+k) % n]

    return "".join(ans)


s = "isudfhkasfasd"
k = 3
print(getEncryptedString(None, s, k))
