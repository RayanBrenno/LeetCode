# A ideia é ordenar as pizzas para facilitar a escolha das maiores. Como em cada dia consumimos 4 pizzas, calculamos o número total de dias. Nos dias ímpares, o ganho corresponde à maior pizza do grupo (Z), então basta somar as maiores pizzas disponíveis, percorrendo o array de trás para frente. Após reservar essas pizzas, nos dias pares o ganho corresponde à segunda maior (Y), então, entre as maiores restantes, pulamos a maior (que será o Z do grupo) e somamos a próxima, avançando duas posições a cada iteração. Dessa forma, maximizamos o ganho total escolhendo sempre as maiores pizzas possíveis para cada tipo de dia.

from typing import List


def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort()
        ans = 0
        index = len(pizzas) - 1
        days = len(pizzas) // 4

        # odd
        for _ in range((days+1)//2):
            ans += pizzas[index]
            index -= 1

        # even
        for _ in range(days//2):
            ans += pizzas[index-1]
            index -= 2

        return ans
    
    
pizzas = [1, 2, 3, 4, 5, 6, 7, 8] 
print(maxWeight(None, pizzas))  # Saída esperada: 18