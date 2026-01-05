from typing import List


def findDifferentBinaryString(nums: List[str]) -> str:

    n = len(nums)
    res = ""

    for x in range(n):
        char = int(nums[x][x])
        aux = "1" if char == 0 else "0"
        res += aux

    return res

    """
    N = len(nums[0])
    aux = [(bin(x)[2:]).zfill(N) for x in range(2**N)]
    dif = set(aux) - set(nums)

    return dif.pop()
    """


nums = [["111", "011", "001"]]
print(findDifferentBinaryString(nums))
