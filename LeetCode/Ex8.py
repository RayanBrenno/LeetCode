def myAtoi(s):
    string = []
    num = "0123456789"
    sign = 1
    boolSign = False
    for x in s:
        if x in "+-" and len(string) == 0 and not boolSign:
            sign = 1 if x == "+" else -1
            boolSign = True
        elif x == " " and (len(string) == 0 and not boolSign):
            continue
        elif x not in num:
            break
        else: 
            string.append(x)
    
    if len(string) > 0:
        value = int(''.join(string)) * sign
        if value >  2**31 - 1: return 2**31 - 1
        
        if value < -(2**31 - 1): return -2**31
        
        else: return value
     
    else: return 0


s = "   -0 123"
print(myAtoi(s))

s = "   -04123"
print(myAtoi(s))

s = "   - 4123"
print(myAtoi(s))
