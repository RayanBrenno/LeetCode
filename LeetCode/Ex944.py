# Bom, o objetivo é verificar as COLUNAS formadas pelas strings e contar quantas precisam ser removidas. Como todas as strings têm o mesmo tamanho, cada posição do índice representa uma coluna. A estratégia é percorrer coluna por coluna, analisando os caracteres daquela mesma posição em todas as strings, de cima para baixo. Se em alguma coluna existir pelo menos um caso em que a letra de uma string é maior do que a letra da string logo abaixo, essa coluna não está ordenada. Quando isso acontece, contamos essa coluna como inválida e seguimos para a próxima. No final, o total de colunas inválidas é a resposta.


from typing import List
def minDeletionSize(strs: List[str]) -> int:
        rows, cols = len(strs), len(strs[0])
        ans = 0

        for x in range(cols):
            for y in range(rows - 1):
                if strs[y][x] > strs[y + 1][x]:
                    ans += 1
                    break

        return ans

strs = ["cba","daf","ghi"]
solution = minDeletionSize(strs)
print(solution)  # Output: 1