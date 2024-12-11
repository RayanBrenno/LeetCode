def finalString(s):
    s = list(s)
    res = ""
    for x in s:
        if x == "i":
            res = res[::-1]
        else:
            res += x
     
    return res

s = "string"
print(finalString(s))