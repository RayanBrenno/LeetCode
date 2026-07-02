# A solução percorre o array procurando a maior subarray que siga a propriedade da sequência de Fibonacci, ou seja, em que cada elemento seja igual à soma dos dois anteriores. Se a condição for satisfeita, a sequência atual é estendida incrementando count; caso contrário, uma nova sequência é iniciada com os dois últimos elementos. Ao longo do percurso, ans armazena o maior comprimento encontrado e é retornado ao final.

from typing import List

def longestSubarray(self, nums: List[int]) -> int:
    n = len(nums)
    if n <= 2:
        return n

    ans = count = 2

    for x in range(2, n):
        if nums[x] == nums[x-1] + nums[x-2]:
            count += 1
        else:
            count = 2
        ans = max(ans, count)

    return ans


nums = [1,1,1,1,2,3,5,1]
print(longestSubarray(None, nums)) 