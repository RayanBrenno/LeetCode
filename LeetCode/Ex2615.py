# A função calcula, para cada posição do array, a soma das distâncias até todas as outras posições que possuem o mesmo valor. Para isso, primeiro agrupa os índices de cada número em um dicionário, onde cada valor aponta para uma lista com suas posições no array. Em seguida, para cada grupo de índices iguais, calcula a soma total desses índices e percorre a lista acumulando um prefixo. Durante esse percurso, usa uma fórmula que combina a soma total, o prefixo e a posição atual para calcular, de forma eficiente, a soma das distâncias até os elementos à esquerda e à direita, evitando comparações repetidas. O resultado é armazenado diretamente na posição correspondente do array resposta, garantindo uma solução otimizada em tempo linear em relação ao tamanho da entrada.

from collections import defaultdict
from typing import List

def distance(self, nums: List[int]) -> List[int]:
    n = len(nums)
    reps = defaultdict(list)

    for index, num in enumerate(nums):
        reps[num].append(index)

    ans = [0] * n

    for rep in reps.values():
        total = sum(rep)
        prefix_total = 0
        aux = len(rep)

        for i, idx in enumerate(rep):
            ans[idx] = total - prefix_total * 2 + idx * (2 * i - aux)
            prefix_total += idx

    return ans


nums = [1, 3, 1, 1, 2]
print(distance(None, nums))