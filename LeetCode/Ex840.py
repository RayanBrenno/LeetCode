#A ideia do algoritmo é percorrer a matriz e verificar, um por um, todos os blocos possíveis de tamanho 3x3. Para cada posição inicial, o código analisa se aquele bloco forma um quadrado mágico válido. Primeiro, ele confere se todos os números do 3x3 estão no intervalo de 1 a 9 e se não há valores repetidos, usando um conjunto para controlar isso. Em seguida, verifica se a soma de cada uma das três linhas, das três colunas e das duas diagonais é igual a 15. Caso qualquer uma dessas verificações falhe, o bloco é descartado. Se todas passarem, o quadrado é considerado mágico e entra na contagem final. No fim, o algoritmo retorna quantos quadrados mágicos 3x3 existem na matriz.

from typing import List

def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        ans = 0

        def magic_grid(r,c):
            #values
            aux = set()
            for i in range(r, r+3):
                for j in range(c, c+3):
                    if grid[i][j] in aux or grid[i][j] > 9:
                        return 0
                    aux.add(grid[i][j])

            #sum rows
            for i in range(r, r+3):
                if sum(grid[i][c:c+3]) != 15:
                    return 0 

            #sum cols
            for j in range(c, c+3):
                if (grid[r][j]+grid[r+1][j]+grid[r+2][j]) != 15:
                    return 0 

            #sum diagonals
            if (grid[r][c]+grid[r+1][c+1]+grid[r+2][c+2] != 15 or grid[r+2][c]+grid[r+1][c+1]+grid[r][c+2] != 15):
                return 0

            return 1 

        for r in range(rows-2):
            for c in range(cols-2):
                ans += magic_grid(r,c)   

        return ans  
    

grid = [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]

print(numMagicSquaresInside(None, grid))