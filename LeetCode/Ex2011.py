# Esse código calcula o valor final de uma variável após uma lista de operações de incremento e decremento. Primeiro ele conta quantas vezes cada operação aparece usando um dicionário. Depois percorre essas operações e, se for "++X" ou "X++", soma a quantidade de vezes que ela apareceu ao resultado; caso contrário (que são "--X" ou "X--"), subtrai essa quantidade. No final, retorna o valor acumulado, que representa o resultado final após todas as operações.

from collections import defaultdict
from typing import List

def finalValueAfterOperations(self, operations: List[str]) -> int:
    # count = Counter(operations)
    dic = defaultdict(int)
    for x in operations:
        dic[x] += 1
    ans = 0
    for x, y in dic.items():
        if x == "++X" or x == "X++":
            ans += 1*y
        else:
            ans -= 1*y
    return ans


operations = ["--X","X++","X++"]
print(finalValueAfterOperations(None, operations))