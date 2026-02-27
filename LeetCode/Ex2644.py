# O algoritmo percorre cada divisor da lista e, para cada um, conta quantos números de nums são divisíveis por ele, incrementando uma pontuação sempre que y % x == 0. Em seguida, armazena pares contendo o divisor e sua respectiva contagem e ordena esses pares priorizando primeiro a maior quantidade de divisões (ordem decrescente) e, em caso de empate, o menor divisor (ordem crescente). Por fim, retorna o divisor que obteve a maior pontuação, garantindo que, se houver empate, o menor valor seja escolhido. A complexidade é O(n * m), onde n é o tamanho de nums e m o de divisors

from typing import List

def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
    count = set()
    for x in divisors:
        aux = 0
        for y in nums:
            aux += 1 if y % x == 0 else 0
        count.add((x, aux))
    count = sorted(count, key=lambda x: (-x[1], x[0]))
    return count[0][0]

nums = [4,7,9,3,9,2,1,3,10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
divisors = [5,2,3,4,1,10,7,11,13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
print(maxDivScore(None, nums, divisors))
