def cellsInRange(s):
    aux = s.split(":")
    res = []
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    curLetter = alfabeto.index(aux[0][0])
    curNum = int(aux[0][1]) - 1

    while alfabeto[curLetter]+str(curNum+1) != aux[1]:
        curNum += 1
        res.append(alfabeto[curLetter]+str(curNum))
        if curNum == int(aux[1][1]):
            curLetter += 1
            curNum = int(aux[0][1]) - 1
    res.append(aux[1])
    return res


s = s = s = "K1:L2"
print(cellsInRange(s))
