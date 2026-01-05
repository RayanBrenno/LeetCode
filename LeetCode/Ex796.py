def rotateString(s, goal):
    
    for x in range(len(s)):
        s = list(s)
        auxValue = len(s)-1
        auxChar = s[auxValue]
        s[auxValue] = s[0]

        while auxValue > 0:
            auxChar, s[auxValue-1] = s[auxValue-1], auxChar
            auxValue -= 1

        s = ''.join(s)
        
        if s == goal:
            return True

    return False


s = "abcde"
goal = "cdeab"
print(rotateString(s, goal))
