import math


def checkIfExist(arr):

    for index, value in enumerate(arr):
        if value/2 in arr and arr.index(index//2) != index:
            return True
    return False
    """
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if j == i: continue
            if arr[i] == 2* arr[j]:
                print(i,j)
                return True
    return False
    """


arr = [-2,0,10,-19,4,6,-8]
print(checkIfExist(arr))
