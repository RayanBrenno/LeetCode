def isValid(s):
    arrOpen = []
    dic = {
        "[": "]",
        "(": ")",
        "{": "}",
    }
    for x in s:
        if x in dic.keys():
            arrOpen.append(x)
        elif len(arrOpen) > 0 and x in dic.values() and dic.get(arrOpen[-1]) == x :
            arrOpen.pop()
        else:
            return False

    bol = True if len(arrOpen) == 0 else False
    return bol


print(isValid("[([]])"))
