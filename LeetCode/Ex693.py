# Esse código verifica se o número possui bits alternados na representação binária. Ele começa pegando o último bit com n & 1, depois desloca o número para a direita. Em seguida, enquanto ainda houver bits, compara o bit atual com o anterior; se forem iguais, significa que não alterna e retorna False. Caso sejam diferentes, atualiza o valor do bit anterior e continua deslocando. Se terminar o loop sem encontrar bits iguais consecutivos, retorna True, indicando que os bits alternam corretamente.

def hasAlternatingBits(self, n: int) -> bool:
    # aux = n & 1
    # n >>= 1
    # while n > 0:
    #     if aux == n & 1:
    #         return False
    #     aux = n & 1
    #     n >>= 1

    # return True

    x = n ^ (n >> 1)
    
    return (x & (x + 1)) == 0



n = 5
print(hasAlternatingBits(None, n))