# Ordenamos o array em ordem decrescente para garantir que estamos sempre tentando formar o triângulo com a maior base possível, já que isso maximiza o perímetro. Em seguida, percorremos os números em grupos de três consecutivos e verificamos a condição do triângulo, onde o maior lado precisa ser menor que a soma dos outros dois. Assim que encontramos o primeiro trio que satisfaz essa regra, já sabemos que ele gera o maior perímetro possível e retornamos a soma dos três lados. Se nenhum trio respeitar essa condição, então não é possível formar um triângulo e o retorno é 0.

from typing import List

def largestPerimeter(self, nums: List[int]) -> int:
    nums.sort(reverse=True)
    for x in range(len(nums) - 2):
        if nums[x] < nums[x+1] + nums[x+2]:
            return nums[x] + nums[x+1] + nums[x+2]

    return 0


nums = [2, 1, 2]
print(largestPerimeter(None, nums))