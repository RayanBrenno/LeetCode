def addSpaces(s, spaces):
    
    res = []
    index = 0
    
    for x in spaces:
        res.append(s[index: x] + " ")
        index = x

    res.append(s[index:])
    return "".join(res)

    """
        countS, countSpaces = 0, 0
        res = []

        while countS < len(s) and countSpaces < len(spaces):
            if countS < spaces[countSpaces]:
                res.append(s[countS])
                countS += 1
            else:
                res.append(" ")
                countSpaces += 1

        if countS < len(s):
            res.append(s[countS:])

        return "".join(res)
    """


s = "LeetcodeHelpsMeLearn"
spaces = [8, 13, 15]
print(addSpaces(s, spaces))
