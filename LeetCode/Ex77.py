from typing import List


def combine(n: int, k: int) -> List[List[int]]:

    aux = [x for x in range(1, n+1)]

    def backtrack(arr, index, k):
        if k == 0:
            res.append(arr[:])
            return
        if index >= len(aux):
            return
        arr.append(aux[index])
        backtrack(arr, index+1, k-1)
        arr.pop()
        backtrack(arr, index+1, k)

    res = []
    backtrack([], 0, k)
    return res


n = 5
k = 4
print(combine(n, k))
