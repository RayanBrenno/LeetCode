def lengthOfLongestSubstring(s):

    unique = {}
    aux = 0
    maxLength = 0
    for x in range(len(s)):

        char = s[x]
        
        if char in unique and unique[char] >= aux:
            aux = unique[char] + 1
            
        else:
            maxLength = max(maxLength, x - aux + 1)
        unique[char] = x

    return maxLength

    """
    uniqueChar = {}
    maxLength = 0
    aux = 0

    if len(s) < 2:
        return len(s)

    for i in range(len(s)):
        if s[i] not in uniqueChar:
            uniqueChar[s[i]] = i
            aux += 1
            if aux > maxLength and i == len(s)-1:
                maxLength, aux = aux, 1
        else:
            if aux > maxLength:
                maxLength, aux = aux, 1
            else:
                aux = 1
            uniqueChar = {}
            uniqueChar[s[i]] = i

    return maxLength if maxLength != 0 else aux
    """


s = "bsfsfbgggggabcdefs"
print(lengthOfLongestSubstring(s))
