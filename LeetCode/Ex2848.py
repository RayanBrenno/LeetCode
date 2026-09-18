# A implementação utiliza um set para armazenar todos os pontos inteiros cobertos pelos carros. Para cada intervalo [x, y], percorre todos os valores de x até y e adiciona cada ponto ao conjunto, evitando automaticamente repetições quando os intervalos se sobrepõem. No final, retorna o tamanho do set, que representa a quantidade total de pontos cobertos.

from typing import List


def numberOfPoints(self, nums: List[List[int]]) -> int:
    ans = set()

    for x, y in nums:
        for num in range(x, y + 1):
            ans.add(num)

    return len(ans)


nums = [[1, 3], [2, 5], [7, 9]]
print(numberOfPoints(nums))  # Saída: 8
