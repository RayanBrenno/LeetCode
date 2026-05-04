# A ideia da solução é perceber que Alice quer maximizar a quantidade de tipos diferentes de doces, mas está limitada a comer apenas metade dos doces do array (n/2). Isso significa que a resposta nunca pode ser maior que n/2, porque ela não pode comer mais doces do que isso, e também nunca pode ser maior que a quantidade de tipos únicos existentes no array. Portanto, basta contar quantos tipos diferentes de doces existem usando um set e retornar o menor valor entre essa quantidade e n/2. Dessa forma garantimos o máximo possível de tipos diferentes respeitando a restrição do médico.

from typing import List

def distributeCandies(self, candyType: List[int]) -> int:
    candy_set = set(candyType)
    n = len(candyType)
    return min(len(candy_set), n//2)


candyType = [1, 1, 2, 2, 3, 3]
print(distributeCandies(None, candyType))