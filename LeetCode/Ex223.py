# A ideia do exercício é calcular a área total de dois retângulos no plano cartesiano. Primeiro calculamos a área de cada retângulo usando (x2 - x1) * (y2 - y1). Porém, se os dois retângulos se sobrepõem, a área da interseção seria contada duas vezes ao somarmos as duas áreas. Então calculamos a largura da interseção no eixo x usando min(ax2, bx2) - max(ax1, bx1) e a altura no eixo y usando min(ay2, by2) - max(ay1, by1). Usamos max(0, ...) para garantir que, caso não exista sobreposição, o valor não fique negativo. A área da interseção é inter_x * inter_y. Por fim, retornamos area1 + area2 - inter_area, removendo a área que foi contada duas vezes.

def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

    area1 = (ax2 - ax1) * (ay2 - ay1)
    area2 = (bx2 - bx1) * (by2 - by1)

    inter_x = max(0, min(ax2, bx2) - max(ax1, bx1))
    inter_y = max(0, min(ay2, by2) - max(ay1, by1))
    inter_area = inter_x * inter_y

    return area1 + area2 - inter_area


ax1 = -3
ay1 = 0
ax2 = 3
ay2 = 4
bx1 = 0
by1 = -1
bx2 = 9
by2 = 2
print(computeArea(None, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2))

# exemplo sem interseção
ax1 = 0
ay1 = 0
ax2 = 2
ay2 = 2
bx1 = 3
by1 = 3
bx2 = 5
by2 = 5
print(computeArea(None, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2))
