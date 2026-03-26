# O algoritmo resolve o problema testando todas as possíveis rotações da matriz mat. Ele começa verificando se a matriz atual já é igual à target; se for, retorna True. Caso contrário, ele rotaciona a matriz 90 graus no sentido horário usando a combinação de inverter as linhas (mat[::-1]) e depois transpor com zip. Esse processo é repetido até 4 vezes, cobrindo as rotações de 0°, 90°, 180° e 270°. Se em alguma dessas rotações a matriz ficar igual à target, o algoritmo retorna True; caso contrário, após testar todas as possibilidades, retorna False.

from typing import List

def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
    for _ in range(4):
        if mat == target:
            return True

        aux = [list(row) for row in zip(*mat)]
        mat = [list(row) for row in zip(*mat[::-1])]
        
        for x in aux:
            print(x)
        print("---")
        for x in mat:
            print(x)
        print("---")

    return False


mat = [[0,0,0],
       [0,1,0],
       [1,1,1]]
target = [[1,1,1],[0,1,0],[0,0,0]]
print(findRotation(None, mat, target))