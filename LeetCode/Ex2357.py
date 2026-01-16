# Esse exercício se resume a observar que cada operação elimina um valor positivo distinto do array. Os zeros não influenciam em nada, e valores repetidos podem ser resolvidos juntos na mesma etapa. Portanto, basta ignorar os zeros e contar quantos números diferentes restam. Esse total é exatamente o número mínimo de operações necessárias.

from typing import List
def minimumOperations(self, nums: List[int]) -> int:
    
    # ans = 0
    # nums.sort()
    # n = 0
    # while n < len(nums):
    #     if nums[n] != 0:
    #         ans += 1
    #         for x in range(n+1, len(nums)):
    #             nums[x] -= nums[n]
    #         nums[n] = 0
    #     n += 1

    # return ans
    
    return len([x for x in set(nums) if x != 0])
    


print(minimumOperations(None, [1,5,0,3,5]))
print(minimumOperations(None, [0,0,0]))