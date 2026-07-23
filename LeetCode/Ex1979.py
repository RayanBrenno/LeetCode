# A solução encontra o menor e o maior elemento do array utilizando min e max. Como o problema pede apenas o máximo divisor comum entre esses dois valores, basta aplicar math.gcd sobre eles e retornar o resultado. Dessa forma, a implementação é simples, direta e eficiente.

from typing import List
from math import gcd

def findGCD(self, nums: List[int]) -> int:
        mx, mn = max(nums), min(nums)
        return gcd(mx, mn)
    
    
nums = [2, 5, 6, 9, 10]
print(findGCD(None, nums))  # Output: 2