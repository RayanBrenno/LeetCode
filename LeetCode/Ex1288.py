# A solução começa ordenando os intervalos pelo início em ordem crescente e, em caso de empate, pelo fim em ordem decrescente, garantindo que intervalos maiores apareçam antes dos menores quando possuem o mesmo início. Em seguida, percorre a lista mantendo o maior valor de término encontrado (end). Se o fim do intervalo atual for maior que end, significa que ele não está coberto por nenhum intervalo anterior, então ele é contado na resposta e end é atualizado. Caso contrário, seu fim é menor ou igual a end, indicando que ele está completamente contido em um intervalo já processado, sendo ignorado. No final, retorna a quantidade de intervalos que não foram cobertos.

from typing import List

def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda x: (x[0], -x[1]))

    ans = 0
    end = 0

    for _, x in intervals:
        if x > end:
            ans += 1
            end = x

    return ans


intervals = [[1, 4], [3, 6], [2, 8]]
print(removeCoveredIntervals(None, intervals))