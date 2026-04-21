# A função transforma o número em uma lista de dígitos e cria um dicionário que armazena a última posição em que cada dígito aparece, permitindo acesso rápido a essas posições; em seguida, percorre cada dígito e, para cada um, tenta encontrar um dígito maior (de 9 até o valor atual +1) que esteja à direita, e ao encontrar essa possibilidade realiza a troca entre as posições para maximizar o valor do número, retornando imediatamente o resultado, e caso nenhuma troca vantajosa seja encontrada, apenas reconstrói e retorna o número original.

def maximumSwap(self, num: int) -> int:
    nums_list = list(str(num))
    occurency = {int(n): index for index, n in enumerate(nums_list)}

    for index, num in enumerate(nums_list):
        for aux in range(9, int(num), -1):
            if aux in occurency and occurency[aux] > index:
                nums_list[index], nums_list[occurency[aux]
                                            ] = nums_list[occurency[aux]], nums_list[index]
                return int("".join(nums_list))

    return int("".join(nums_list))


num = 2736
print(maximumSwap(None, num))
