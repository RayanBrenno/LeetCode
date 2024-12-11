def makeFancyString(s):

    if len(s) < 3:
        return s
    s = list(s)
    for x in range(len(s)-2, 0, -1):
        if s[x-1] == s[x] == s[x+1]:
            s.pop(x)

    return ''.join(s)

s = "aaabaaaa"
print(makeFancyString(s))
