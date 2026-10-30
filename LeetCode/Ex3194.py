# A ideia é ordenar o array e utilizar dois ponteiros, left e right, começando nas extremidades. A cada iteração, calculamos a média entre o menor e o maior elemento e atualizamos ans caso essa média seja menor que a encontrada anteriormente. Em seguida, aproximamos os ponteiros, avançando left e diminuindo right, até que todos os pares sejam analisados. No final, retornamos a menor média encontrada.

from typing import List


def minimumAverage(self, nums: List[int]) -> float:
    ans = float('inf')
    left, right = 0, len(nums) - 1
    nums.sort()

    while left < right:
        ans = min(ans, (nums[left] + nums[right]) / 2)
        left += 1
        right -= 1

    return ans



nums = [1, 2, 3, 4, 5]
print(minimumAverage(None, nums))