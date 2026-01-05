def maxScore(s: str) -> int:
    res = 0
    countZero = 0
    countOne = s.count("1")
    
    for x in range(len(s)-1):
        if s[x] == "0": countZero+=1
        else: countOne-=1
        res = max(res, countOne+countZero)
    
    return res 


s = "011101"
print(maxScore(s))