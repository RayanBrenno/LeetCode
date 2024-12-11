def reverseStr(s, k):
    res = []
    index = 0
    reverse = True
    for x in range(k, len(s), k):
        if reverse:
            res.append(s[index:x][::-1])
            reverse = False
        else:
            res.append(s[index:x])
            reverse = True
        index = x

    res = "".join(res)
    if len(res) < len(s):
        return res + s[index:][::-1] if reverse else res + s[index:]

    return res


s = "abcdefg"
k = 4
print(reverseStr(s, k))
