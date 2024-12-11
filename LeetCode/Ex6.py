def convert(s, numRows):
    rows = [[] for x in range(numRows)]
    finalString = ""
    contAux = 0
    bolAux = True
    
    if numRows == 1 or numRows >= len(s):
        return s
    
    for i in s:
        if bolAux:
            rows[contAux].append(i)
            contAux+=1
        else:
            rows[contAux].append(i)
            contAux-=1
        
        if contAux == 0:bolAux = True  
        elif contAux == numRows-1:bolAux = False

    for i in range(len(rows)):
        finalString += ''.join(rows[i])

    return finalString


s = "PAYPALISHIRING"
numRows = 4
print(convert(s, numRows))
