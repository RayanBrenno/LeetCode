def isSubsequence(s, t):
    if len(s) == 0:
        return True
    count = 0
    for x in t:
        if count < len(s) and x == s[count]:
            count += 1
    return count == len(s)


s = "abc"
t = "ahbgdc"
print(isSubsequence(s, t))
