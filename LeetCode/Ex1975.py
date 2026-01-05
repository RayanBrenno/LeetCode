# A ideia é percorrer toda a matriz calculando a soma dos valores absolutos, ao mesmo tempo em que contamos a quantidade de números negativos e rastreamos o menor valor absoluto encontrado. Isso porque podemos multiplicar qualquer elemento por -1 para maximizar a soma total da matriz. 
# Se a quantidade de números negativos for par, é possível transformar todos em positivos, e a maior soma será simplesmente a soma dos valores absolutos.
# Porém, se a quantidade de negativos for ímpar, obrigatoriamente um valor precisará permanecer negativo. Para minimizar a perda na soma, escolhemos deixar negativo o elemento com o menor valor absoluto.
# Assim, ao final, se o número de negativos for par, retornamos a soma total dos valores absolutos. Caso seja ímpar, subtraímos duas vezes o menor valor absoluto da soma total para ajustar corretamente o resultado.
def maxMatrixSum(matrix):
    min_value = float('inf')
    total_sum = 0
    neg_count = 0

    for row in matrix:
        for value in row:
            if value < 0:
                neg_count += 1
            abs_value = abs(value)
            min_value = min(min_value, abs_value)
            total_sum += abs_value

    if neg_count % 2 == 0:
        return total_sum
    return total_sum - 2 * min_value


matrix = [[1, 2, 3], [-1, -2, -3], [1, 2, 3]]
print(maxMatrixSum(matrix))
