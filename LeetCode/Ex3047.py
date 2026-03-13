# A ideia do exercício é encontrar a maior área de um quadrado formado pela interseção de dois retângulos. Para isso, percorremos todos os pares de retângulos. Cada retângulo é definido por dois pontos: bottomLeft (canto inferior esquerdo) e topRight (canto superior direito). Para cada par, calculamos a região de interseção usando a lógica de intervalos: o início da interseção é o max entre os limites mínimos e o fim é o min entre os limites máximos. Se inter_min_x < inter_max_x e inter_min_y < inter_max_y, significa que existe sobreposição. A largura e altura da interseção são calculadas pelas diferenças desses valores, e o maior quadrado possível dentro dessa região terá lado igual ao menor entre largura e altura. Mantemos o maior lado encontrado em ans e no final retornamos ans * ans (área do quadrado). O código também usa uma otimização, pulando retângulos cujo tamanho já é menor que o melhor lado encontrado, pois eles não conseguiriam gerar um quadrado maior.

from typing import List


def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
    ans = 0
    n = len(bottomLeft)

    for x in range(n):
        min_x1, min_y1 = bottomLeft[x]
        max_x1, max_y1 = topRight[x]

        # IMPORTANT
        if max_x1 - min_x1 < ans or max_y1 - min_y1 < ans:
            continue

        for y in range(x+1, n):

            min_x2, min_y2 = bottomLeft[y]
            max_x2, max_y2 = topRight[y]

            inter_min_x = max(min_x1, min_x2)
            inter_max_x = min(max_x1, max_x2)
            inter_min_y = max(min_y1, min_y2)
            inter_max_y = min(max_y1, max_y2)

            if inter_min_x < inter_max_x and inter_min_y < inter_max_y:
                aux = min(inter_max_x - inter_min_x, inter_max_y - inter_min_y)
                ans = max(ans, aux)

    return ans*ans

    # ans = 0
    # n = len(bottomLeft)

    # for x in range(n):
    #     for y in range(x+1, n):

    #         inter_min_x = max(bottomLeft[x][0], bottomLeft[y][0])
    #         inter_max_x = min(topRight[x][0], topRight[y][0])

    #         inter_min_y = max(bottomLeft[x][1], bottomLeft[y][1])
    #         inter_max_y = min(topRight[x][1], topRight[y][1])

    #         if inter_min_x < inter_max_x and inter_min_y < inter_max_y:
    #             aux = min(inter_max_x - inter_min_x, inter_max_y - inter_min_y)
    #             ans = max(ans, aux)

    # return ans*ans
    return


bottomLeft = [[1,1],[2,2],[3,1]]
topRight = [[3,3],[4,4],[6,6]]
print(largestSquareArea(None, bottomLeft, topRight))
