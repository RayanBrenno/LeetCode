def titleToNumber(columnTitle):

    columnTitle = columnTitle[::-1]
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = 0
    for x in range(len(columnTitle)):
        res += (alfabeto.index(columnTitle[x])+1) * (26**x)

    """
    columnTitle = columnTitle[::-1]
    alfabeto = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 
        'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 
        'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 
        'Z': 26
    }
    res = 0
    for x in range(len(columnTitle)):
        res+= alfabeto[columnTitle[x]] * (26**x)
    """
    return res


columnTitle = "AA"
print(titleToNumber(columnTitle))
