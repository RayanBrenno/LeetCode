def countPalindromicSubsequence(s: str) -> int:
    
    used = set()
    res, n = 0, len(s)
    
    for x in range(n-2):
        char = s[x]
        if char in used:
            continue
        j = n - 1
        while j - 1 > x:
            if s[j] == char:
                aux = set(s[x+1:j])
                used.add(char)
                res += len(aux)
                break
            j -= 1         

    return res


s = "bbcbabaabza"
print(countPalindromicSubsequence(s))
