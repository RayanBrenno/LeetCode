def minChanges(s):
    count = 0
    for x in range(0, len(s), 2):
        if s[x] != s[x + 1]:
            count += 1
    return count

s = "1001"
minChanges(s)