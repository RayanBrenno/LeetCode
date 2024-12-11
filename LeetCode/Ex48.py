def rotate(matrix):

    aux = [[]for x in range(len(matrix))]
    for i in range(len(matrix[0]), 0, -1):
        valAux = 0
        for j in matrix[i-1]:
            aux[valAux].append(j)
            valAux += 1

    matrix = aux
    return matrix




matrix = [[1, 2, 3], [4,5,6],[7,8,9]]
print(rotate(matrix))

matrix = [[5, 1, 9, 11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(rotate(matrix))
