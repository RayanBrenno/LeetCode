def reverseVowels(s):
    vowels = "aeiouAEIOU"
    right, left = 0 , len(s)-1
    s = list(s)
    while right < left:
        if s[left] not in vowels:
            left-=1
        if s[right] not in vowels:
            right+=1
        if s[left] in vowels and s[right] in vowels:
            s[right], s[left] = s[left], s[right]
            left-=1
            right+=1
        
    return "".join(s)
    
    
    """
    vowels = ["A", "E", "I", "O", "U"]
    foundVowels = []
    for x in s:
        if x.upper() in vowels:
            foundVowels.append(x)

    s = list(s)
    foundVowels = foundVowels[::-1]
    count = 0
    for x in range(len(s)):
        if s[x].upper() in vowels:
            s[x] == foundVowels[count]
            count += 1
    return "".join(s)
    """

s = "IceCreAm"
print(reverseVowels(s))
