# A implementação simula a passagem do travesseiro usando `ans` para representar a posição atual e `aux` para controlar a direção. Enquanto `aux` é `True`, a posição aumenta até chegar em `n`, quando a direção é invertida; depois, a posição diminui até chegar em `1`, invertendo novamente a direção. O processo é repetido `time` vezes e, ao final, `ans` representa a posição onde o travesseiro está.


def passThePillow(self, n: int, time: int) -> int:
    aux = True
    ans = 1

    for _ in range(time):
        if aux:
            ans += 1
            if ans == n:
                aux = False
        else:
            ans -= 1
            if ans == 1:
                aux = True

    return ans


n = 4
time = 5
print(passThePillow(n, time))  # Output: 2
