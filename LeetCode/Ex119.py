def getRow(rowIndex):
    output = []

    for x in range(rowIndex+2):
        aux = []
        for y in range(x):
            if y == 0 or y+1 == x:
                aux.append(1)
            else:
                valAux = output[x-1][y-1] + output[x-1][y]
                aux.append(valAux)
        output.append(aux)
    
    output.pop(0)
    return output[rowIndex]


rowIndex = 0
print(getRow(rowIndex))
