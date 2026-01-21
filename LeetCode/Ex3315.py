# O while serve para percorrer os bits ligados do número começando pelo bit menos significativo. Usando o operador & com a variável d, que é sempre uma potência de dois, o código testa se o bit atual está ligado. Enquanto esse bit for 1, o loop continua. Dentro do laço, o valor d é subtraído do número original para desligar exatamente aquele bit, gerando um possível candidato que é armazenado em aux. Em seguida, d é deslocado para a esquerda para testar o próximo bit. O laço termina quando encontra o primeiro bit 0, pois esse é o ponto correto onde a propagação do carry do +1 deve parar. Assim, ao desligar apenas bits dentro desse bloco final de 1s, garante-se que o OR entre aux e aux + 1 reconstrua o número original.

from typing import List

def minBitwiseArray(self, nums: List[int]) -> List[int]:
    ans = []
    for i in range(len(nums)):
        aux = -1
        d = 1
        if nums[i] % 2 != 0:
            while (nums[i] & d) != 0:
                aux = nums[i] - d
                d <<= 1
        ans.append(aux)

    return ans


nums = [2, 3, 5, 7, 1200557]
print(minBitwiseArray(None, nums))