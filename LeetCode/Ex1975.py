def maxMatrixSum(matrix):
    for x in matrix:
        if min(x) > 0:
            print(x)


matrix = [[1, 2, 3], [-1, -2, -3], [1, 2, 3]]
print(maxMatrixSum(matrix))
