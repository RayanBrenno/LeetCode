from collections import defaultdict
from typing import List


def firstCompleteIndex(arr: List[int], mat: List[List[int]]) -> int:

    m, n = len(mat), len(mat[0])
    dic = {}
    for x in range(m):
        for y in range(n):
            dic[mat[x][y]] = (x, y)

    cols = [0] * n
    rows = [0] * m
    
    for x in range(len(arr)):
        row, col = dic[arr[x]]
        print(row, col)
        rows[row] += 1
        cols[col] += 1
        if rows[row] == n or cols[col] == m:
            return x

    """
    dic = defaultdict(list)
    cols = defaultdict(int)
    rows = defaultdict(int)
    m, n = len(mat), len(mat[0])
    for x in range(m):
        for y in range(n):
            aux = mat[x][y]
            dic[aux] = [x, y]

    for x in range(len(arr)):
        row, col = dic[arr[x]]
        rows[row] += 1
        cols[col] += 1
        if rows[row] == n or cols[col] == m:
            return x
    """

arr = [6,2,3,1,4,5]
mat = [[5,1],[2,4],[6,3]]
print(firstCompleteIndex(arr, mat))
