# Esse exercício busca o maior produto possível de três números do array. A sacada é perceber que esse valor pode vir de dois cenários: ou dos três maiores números (todos positivos), ou da combinação de dois números negativos (que viram positivo ao multiplicar) com o maior número positivo. O código ordena o array para facilitar o acesso a esses valores extremos e então compara essas duas possibilidades, retornando a maior. É uma solução simples e eficiente, embora o uso de ordenação traga um custo de O(n log n), podendo ser otimizado para O(n) ao rastrear apenas os maiores e menores valores durante uma única passagem.

from typing import List

def maximumProduct(self, nums: List[int]) -> int:
    max1 = max2 = max3 = float('-inf')
    min1 = min2 = float('inf')

    for x in nums:

        if x > max1:
            max1, max2, max3 = x, max1, max2
        elif x > max2:
            max2, max3 = x, max2
        elif x > max3:
            max3 = x

        if x < min1:
            min1, min2 = x, min1
        elif x < min2:
            min2 = x

    return max(max1 * max2 * max3, max1 * min1 * min2)

    # nums.sort() 
    # return max(nums[-1]*nums[-2]*nums[-3], nums[-1]*nums[0]*nums[1])
    
    
nums = [1,2,3]
print(maximumProduct(None, nums))