# Bom, o objetivo é distribuir todas as maçãs usando a menor quantidade possível de caixas.
# Como as maçãs podem ser divididas entre várias caixas, a melhor estratégia é utilizar primeiro as caixas com maior capacidade.
# Para isso, ordenamos o array capacity em ordem decrescente e vamos preenchendo essas caixas até que todas as maçãs sejam distribuídas.
# Assim que a soma das capacidades das caixas escolhidas for suficiente para armazenar todas as maçãs, obtemos o menor número de caixas necessário.

from typing import List
def minimumBoxes(apple: List[int], capacity: List[int]) -> int:
    totalApples = sum(apple)
    capacity.sort(reverse=True)

    for index, capacity in enumerate(capacity):
        if capacity >= totalApples:
            return index+1
        totalApples -= capacity

    return -1

apple = [1,3,2]
capacity = [4,3,1,5,2]
print(minimumBoxes(apple, capacity))
