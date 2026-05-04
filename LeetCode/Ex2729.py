# O algoritmo concatena os valores de n, 2n e 3n em uma única string e depois verifica se, ao ordenar seus dígitos, o resultado é exatamente "123456789". Se for igual, significa que a concatenação usa todos os dígitos de 1 a 9 exatamente uma vez, então retorna True; caso contrário, retorna False.

def isFascinating(self, n: int) -> bool:

    nums = "".join(str(x) for x in range(1, 10))
    aux = str(n) + str(n*2) + str(n*3)
    return nums == "".join(sorted(aux))


    # aux = str(n) + str(n*2) + str(n*3)
    # if len(aux) != 9:
    #     return False

    # nums = list("123456789")
    # for x in aux:
    #     if x not in nums:
    #         return False
    #     nums.remove(x)

    # return True


n = 192
print(isFascinating(None, n))