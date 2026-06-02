# O código testa todas as combinações possíveis entre uma atividade terrestre (land) e uma aquática (water). Para cada par, ele calcula dois cenários: fazer a atividade terrestre primeiro e depois a aquática, ou fazer a aquática primeiro e depois a terrestre. Em cada caso, utiliza max() para garantir que a segunda atividade só comece quando tanto a primeira tiver terminado quanto o horário de início permitido da segunda tiver sido alcançado. O menor tempo final encontrado entre todas as combinações é retornado.

from typing import List

def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
    n = len(landStartTime)
    m = len(waterStartTime)
    res = float("inf")
    for x in range(n):
        for y in range(m):
            land = landStartTime[x] + landDuration[x]
            land_water = max(land, waterStartTime[y]) + waterDuration[y]
            res = min(res, land_water)

            water = waterStartTime[y] + waterDuration[y]
            water_land = max(water, landStartTime[x]) + landDuration[x]
            res = min(res, water_land)

    return res
