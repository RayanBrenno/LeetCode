# Bom, o objetivo é calcular o menor tempo necessário para visitar todos os pontos em ordem. Como é permitido andar na horizontal, vertical e diagonal, em um segundo é possível reduzir a diferença em x e y ao mesmo tempo. Para ir de um ponto ao próximo, o tempo mínimo necessário será o maior valor entre a distância horizontal (|x1 - x2|) e a distância vertical (|y1 - y2|). Isso acontece porque os movimentos diagonais resolvem as duas direções de uma vez, e o que sobra é a maior das duas distâncias. Assim, somamos esse tempo mínimo para cada par de pontos consecutivos e obtemos o tempo total para visitar todos os pontos.
from typing import List

def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
    ans = 0
    for x in range(len(points)-1):
        x1, y1 = points[x]
        x2, y2 = points[x+1]
        ans += max(abs(x1-x2), abs(y1-y2))
    return ans


points = [[1,1],[3,4],[-1,0]]
print(minTimeToVisitAllPoints(None, points))