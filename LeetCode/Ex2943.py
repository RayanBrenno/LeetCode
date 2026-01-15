# A ideia é descobrir o maior espaço contínuo que pode ser aberto tanto na horizontal quanto na vertical. Para isso, ordenamos as barras removidas e percorremos cada lista contando o maior grupo de barras consecutivas, pois barras seguidas criam um vão maior. No final, o lado do maior quadrado possível é definido pela menor sequência entre horizontal e vertical, já que o quadrado precisa caber nas duas direções. Esse lado é ajustado com +1 e a área é calculada elevando ao quadrado.


from typing import List

def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
    hBars.sort()
    vBars.sort()
    hmax, hcur = 1, 1
    vmax, vcur = 1, 1

    for x in range(1, len(hBars)):
        if hBars[x] == hBars[x - 1] + 1:
            hcur += 1
        else:
            hcur = 1
        hmax = max(hmax, hcur)

    for x in range(1, len(vBars)):
        if vBars[x] == vBars[x - 1] + 1:
            vcur += 1
        else:
            vcur = 1
        vmax = max(vmax, vcur)

    return (min(hmax, vmax) + 1)**2


n = 3
m = 3
hBars = [1, 2]
vBars = [2]
print(maximizeSquareHoleArea(None, n, m, hBars, vBars))