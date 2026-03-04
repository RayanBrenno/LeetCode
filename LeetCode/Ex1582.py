# Esse exercício percorre a matriz contando quantos 1 existem em cada linha e em cada coluna usando dois dicionários (dic_row e dic_col). Primeiro, ele faz uma varredura completa para registrar a quantidade de 1s por linha e por coluna. Depois, percorre a matriz novamente e, sempre que encontra um 1, verifica se naquela linha e naquela coluna existe apenas um único 1. Se sim, esse elemento é considerado “especial” e incrementa a resposta. No final, retorna o total de posições que possuem 1 e são as únicas da sua linha e da sua coluna.

from typing import List

def numSpecial(self, mat: List[List[int]]) -> int:
    
    ans = 0
    dic_row = {}
    dic_col = {}
    
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                dic_row[i] = dic_row.get(i, 0) + 1
                dic_col[j] = dic_col.get(j, 0) + 1
    
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1 and dic_row[i] == 1 and dic_col[j] == 1:
                ans += 1
    
    return ans


mat = [[1,0,0],[0,1,0],[0,0,1]]
print(numSpecial(None, mat))