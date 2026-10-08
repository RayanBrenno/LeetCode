# A implementação converte cada letra para seu valor alfabético usando `ord(x) - 96`, calcula a soma total dos valores e verifica se ela é par. Em seguida, percorre os valores acumulando a soma em `aux` e retorna `True` caso encontre um ponto em que a soma acumulada seja exatamente metade da soma total; se ultrapassar essa metade, interrompe o laço com `break`, retornando `False` ao final caso não encontre uma divisão equilibrada.


def scoreBalance(self, s: str) -> bool:
    arr = [ord(x)-96 for x in s]
    print(arr)
    totalSum = sum(arr)
    aux = 0
    if totalSum % 2 == 1:
        return False

    for num in arr:
        aux += num
        if aux == totalSum // 2:
            return True
        elif aux > totalSum // 2:
            break

    return False


s = "abccba"
print(scoreBalance(None, s))  # Saída esperada: True