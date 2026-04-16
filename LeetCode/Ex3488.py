# A solução organiza os índices de cada número em um dicionário e, para lidar com o array circular, “estica” cada lista de posições adicionando o último índice menos n no início e o primeiro índice mais n no final, transformando o problema circular em linear; em seguida, para cada query, obtém o valor correspondente, verifica se ele aparece apenas uma vez (caso em que retorna -1) e, caso contrário, usa busca binária para localizar a posição do índice da query na lista e calcula a menor distância considerando apenas os vizinhos imediato à esquerda e à direita, já que, com a lista expandida, essas diferenças simples já representam corretamente a menor distância no círculo sem precisar de abs ou operações modulares.`

from collections import defaultdict
from typing import List
from pyparsing import nums


def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
    n = len(nums)
    nums_pos = defaultdict(list)

    for i in range(n):
        nums_pos[nums[i]].append(i)

    for pos in nums_pos.values():
        x = pos[0]
        pos.insert(0, pos[-1] - n)
        pos.append(x + n)

    for i in range(len(queries)):
        x = nums[queries[i]]
        pos_list = nums_pos[x]
        if len(pos_list) == 3:
            queries[i] = -1
            continue
        pos = bisect.bisect_left(pos_list, queries[i])
        queries[i] = min(
            pos_list[pos + 1] - pos_list[pos],
            pos_list[pos] - pos_list[pos - 1],
        )

    return queries


nums = [14, 14, 4, 2, 19, 19, 14, 19, 14]
queries = [2, 4, 8, 6, 3]
print(solveQueries(None, nums, queries))
