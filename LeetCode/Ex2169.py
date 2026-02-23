# O código conta quantas operações de subtração seriam feitas entre dois números até que um deles vire zero. Enquanto os dois números forem diferentes de zero (num1 * num2 != 0), ele sempre pega o maior e verifica quantas vezes o menor cabe dentro dele usando divisão inteira (//). Esse valor representa quantas subtrações poderiam ser feitas de uma vez só, então ele soma isso em ans. Depois, atualiza o número maior com o resto da divisão (%), que equivale ao que sobraria após essas subtrações. O processo continua até que um dos números vire zero, e o total acumulado em ans é retornado.

def countOperations(self, num1: int, num2: int) -> int:     
    # res = 0
    # while num1*num2 != 0:
    #     if num1 >= num2:
    #         num1 -= num2
    #     else:
    #         num2 -= num1
    #     res += 1
    # return res
    
    ans = 0

    while num1 * num2 != 0:   
        if num1 >= num2:
            ans += num1 // num2
            num1 %= num2
        else:
            ans += num2 // num1
            num2 %= num1

    return ans

num1 = 10
num2 = 3
print(countOperations(None, num1, num2))