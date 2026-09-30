# A implementação percorre os números de `1` até `n` e, para cada valor, verifica sua divisibilidade por 3 e 5. Quando é divisível por ambos, adiciona `"FizzBuzz"`; quando apenas por 3, adiciona `"Fizz"`; quando apenas por 5, adiciona `"Buzz"`; caso contrário, adiciona o próprio número convertido para string. Ao final, retorna a lista `ans` com todos os resultados.


def fizzBuzz(self, n: int) -> list[str]:
    # aux = [15, 3, 5]
    # ans = []
    # for x in range(1, n + 1):
    #     if x in aux:
    #         if x == aux[0]:
    #             ans.append("FizzBuzz")
    #             aux[0] += 15
    #             aux[1] += 3
    #             aux[2] += 5
    #         elif x == aux[1]:
    #             ans.append("Fizz")
    #             aux[1] += 3
    #         else:
    #             ans.append("Buzz")
    #             aux[2] += 5
    #     else: ans.append(str(x))
    # return ans
    ans = []

    for x in range(1, n+1):
        if x % 3 == 0 and x % 5 == 0:
            ans.append("FizzBuzz")
        elif x % 3 == 0:
            ans.append("Fizz")
        elif x % 5 == 0:
            ans.append("Buzz")
        else:
            ans.append(str(x))

    return ans


n = 15
print(fizzBuzz(None, n))  