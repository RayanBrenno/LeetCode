# A ideia é sempre garantir que o menor custo possível seja obtido escolhendo os menores valores disponíveis. Primeiro, o valor inicial obrigatório é somado à resposta. Em seguida, os demais valores são organizados em uma heap mínima para facilitar o acesso aos menores elementos, e os dois menores são retirados e somados ao custo final.
from typing import List
import heapq

def minimumCost(self, nums: List[int]) -> int:
    if len(nums) == 3:
        return sum(nums)
    ans = nums[0]
    nums.pop(0)
    heapq.heapify(nums)
    
    ans += heapq.heappop(nums)
    ans += heapq.heappop(nums)
    
    return ans



nums = [4, 2, 3, 6, 5]
print(minimumCost(None, nums))  # Example usage