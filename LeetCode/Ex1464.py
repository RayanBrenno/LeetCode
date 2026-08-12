# A solução ordena o array em ordem crescente e, como os dois maiores valores estarão nas duas últimas posições, basta pegar nums[-1] e nums[-2], subtrair 1 de cada e multiplicá-los para obter o produto máximo possível.

from typing import List


def maxProduct(self, nums: List[int]) -> int:
    nums.sort()
    return (nums[-1]-1)*(nums[-2]-1)


nums = [3, 4, 5, 2]
print(maxProduct(None, nums))
