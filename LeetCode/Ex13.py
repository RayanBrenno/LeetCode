def romanToInt(s):
    value = 0
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for x in range(len(s)):
        if x+1 < len(s) and dic.get(s[x]) < dic.get(s[x+1]):
            value -= dic.get(s[x])

        else: value +=dic.get(s[x])
        print(value)

    return value

print(romanToInt('MCMXCIV'))