# A solução trata alguns casos específicos: quando k é igual ao tamanho do array, existe apenas um subarray, então basta retornar o maior elemento; quando k é 1, cada elemento forma seu próprio subarray, então procuramos o maior número que aparece exatamente uma vez usando um Counter; nos demais casos, apenas os elementos das extremidades nums[0] e nums[-1] podem aparecer em exatamente um subarray de tamanho k, então verificamos se cada um ocorre uma única vez e guardamos o maior deles. Caso nenhum seja válido, retornamos -1.

from collections import Counter
from typing import List

def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counter = Counter(nums)

        if k == n:
            return max(nums)
        if k == 1:
            return max((x for x in nums if counter[x] == 1), default=-1)

        ans = -1
        if counter[nums[0]] == 1:
            ans = nums[0]
        if counter[nums[-1]] == 1:
            ans = max(ans, nums[-1])
        return ans

        # if k == len(nums):
        #     return max(nums)
        # counter = Counter()
        # n = len(nums)
        # for x in range(n - k + 1):
        #     aux = set(nums[x : x+k])
        #     for y in aux:
        #         counter[y] += 1
        
        # ans = -1
        # for x in counter:
        #     if counter[x] == 1:
        #         ans = max(ans, x)

        # return ans
        
        
nums = [1, 2, 3, 4, 5]
k = 3
print(largestInteger(None, nums, k))