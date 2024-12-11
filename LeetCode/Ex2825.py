def canMakeSubsequence(str1, str2):
    i, j = 0, 0
    str1, str2 = list(set(str1)), list(set(str2))

    while i < len(str1) and j < len(str2):
        numVal1 = ord(str1[i])
        numVal2 = ord(str2[j])
        print(numVal1)
        print(numVal2)
        print((numVal2 - numVal1 + 26) % 26)
        print("")
        if (numVal2 - numVal1 + 26) % 26 <= 1:
            j += 1
        i += 1

    return j == len(str2)


str1 = "zc"
str2 = "ad"
print(canMakeSubsequence(str1, str2))
