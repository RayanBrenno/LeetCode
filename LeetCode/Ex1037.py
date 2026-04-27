# A solução separa as coordenadas dos três pontos e verifica se eles estão alinhados comparando suas inclinações de forma implícita. Em vez de dividir para calcular a inclinação entre os pares de pontos, usa multiplicação cruzada para evitar divisão por zero: se (y2 - y1) * (x3 - x1) for diferente de (y3 - y1) * (x2 - x1), então os pontos não estão na mesma reta, formam um triângulo e portanto constituem um boomerang; caso os valores sejam iguais, os pontos são colineares e a resposta é falsa.

from typing import List


def isBoomerang(self, points: List[List[int]]) -> bool:
    x1, y1 = points[0]
    x2, y2 = points[1]
    x3, y3 = points[2]

    return (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1)


points = [[1, 1], [2, 3], [3, 2]]
print(isBoomerang(None, points))
