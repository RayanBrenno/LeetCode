from typing import List


def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:

    for index, flower in enumerate(flowerbed):
        if flower == 0 and (index == 0 or flowerbed[index - 1] == 0) and (index == len(flowerbed) - 1 or flowerbed[index + 1] == 0):
            flowerbed[index] = 1
            n -= 1
            if n == 0:  
                return True
    return n == 0 


flowerbed = [1,0,0,0,0,1]
n = 1
print(canPlaceFlowers(flowerbed, n))
