def numMatchingSubseq(s, words):
    res = 0
    for t in words:
        count = 0
        for x in s:
            if count < len(t) and x == t[count]:
                count += 1
            if count == len(t):
                res += 1
                break
    return res


s = "abcde"
words = ["a", "bb", "acd", "ace"]
print(numMatchingSubseq(s, words))
