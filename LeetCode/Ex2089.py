# A solução começa ordenando o array para que todos os valores iguais fiquem agrupados. Em seguida, conta quantos elementos são menores que target, obtendo assim a primeira posição em que ele aparece no array ordenado. Depois, conta quantas vezes target ocorre. Com essas duas informações, basta gerar uma lista contendo todos os índices desde a primeira ocorrência até a última, retornando as posições onde o valor target aparece no array ordenado.

from typing import List

def targetIndices(self, nums: List[int], target: int) -> List[int]:
    
    # nums.sort()
    # if target not in nums:
    #     return []
    # x = nums.index(target)
    # ans = [x]
    # while x + 1 < len(nums) and nums[x + 1] == target:
    #     x += 1
    #     ans.append(x)
    # return ans
    
    nums.sort()
    start = sum(1 for x in nums if x < target)
    rep = nums.count(target)
    return [x for x in range(start, start + rep)]


nums = [1, 2, 5, 2, 3]
target = 2
print(targetIndices(None, nums, target))  # Output: [1, 2]
