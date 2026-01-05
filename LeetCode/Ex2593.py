from typing import List


def findScore(nums: List[int]) -> int:

    visited = set()
    score = 0
    nums = sorted([(index, value)
                  for index, value in enumerate(nums)], key=lambda x: x[1])
    for index, value in nums:
        if index not in visited:
            score += value
            visited.add(index)
            visited.add(index + 1)
            visited.add(index - 1)

            print(f"{visited=}, {index=}, {value=}")

    return score

    """
    score = 0
    visited = set()
    while len(visited) < len(nums):

        aux = float('inf')
        auxIndex = -1


        for index, value in enumerate(nums):
            if index not in visited and value < aux:
                aux = value
                auxIndex = index
            
        if auxIndex == -1: break
        visited.add(auxIndex)
        visited.add(auxIndex + 1 if auxIndex + 1 < len(nums) else auxIndex )
        visited.add(auxIndex - 1 if auxIndex - 1 >= 0  else auxIndex )
        score += aux
    return score
    """


nums = [10, 44, 10, 8, 48, 30, 17, 38, 41,
        27, 16, 33, 45, 45, 34, 30, 22, 3, 42, 42]
print(findScore(nums))
