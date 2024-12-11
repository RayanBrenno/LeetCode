def minimumTotal(triangle):
    output = [[0]*(len(triangle) + 1)]
    triangle = triangle[::-1]

    for x in range(len(triangle)):
        aux = []
        for index, value in enumerate(triangle[x]):
            aux.append(value + min(output[x][index], output[x][index+1]))
        output.append(aux)

    return output[-1][0]

    """
    output = [0]*(len(triangle) + 1)
    for x in triangle[::-1]:
        for index, value in enumerate(x):
            output[index] = value + min(output[index], output[index+1])
    return output[0]
    """

triangle = [[-1], [2, 3], [1, -1, -3]]
print(minimumTotal(triangle))
