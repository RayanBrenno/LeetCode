# A implementação separa as coordenadas dos dois retângulos e verifica se existe sobreposição comparando os limites dos eixos X e Y. Para haver interseção, o início de um retângulo precisa estar antes do fim do outro em ambos os eixos, garantindo que as áreas realmente se cruzem.

from typing import List


def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
    x1, y1, x2, y2 = rec1
    X1, Y1, X2, Y2 = rec2
    return x1 < X2 and X1 < x2 and y1 < Y2 and Y1 < y2


rec1 = [0, 0, 2, 2]
rec2 = [1, 1, 3, 3]
print(isRectangleOverlap(rec1, rec2))  # Saída: True
