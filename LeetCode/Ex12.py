def intToRoman(num):
    string = "" 
    value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    cont = 0
    
    while num > 0:
        if num - value[cont]>=0:
            num -= value[cont]
            string = string + roman[cont]
        else: cont +=1
    return string

num = 75
print(intToRoman(num))
