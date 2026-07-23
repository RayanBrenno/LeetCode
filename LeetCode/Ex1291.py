# A solução gera todos os números sequenciais possíveis utilizando a string "123456789". Para cada tamanho de número, de 1 até 9 dígitos, são extraídas todas as substrings consecutivas, como 12, 23, 123, 2345 e assim por diante. Cada substring é convertida para inteiro e, caso esteja dentro do intervalo [low, high], é adicionada à resposta. Como existem apenas 36 números sequenciais possíveis, a quantidade de operações é constante, resultando em uma solução simples e com complexidade O(1).

from typing import List

def sequentialDigits(self, low: int, high: int) -> List[int]:
    nums = "123456789"
    ans = []

    for x in range(1, 10):
        for y in range(10 - x):
            aux = int(nums[y:y+x])
            if low <= aux <= high:
                ans.append(aux)

    return ans


low = 100
high = 300
print(sequentialDigits(None, low, high))  # Output: [123, 234]