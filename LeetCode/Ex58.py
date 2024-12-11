def lengthOfLastWord(s):

    s = s[::-1]
    bolAux = False
    cont = 0
    for x in s:
        if x == " ":
            if bolAux : break
            continue
        else:
            cont+=1
            bolAux = True
        
    return cont

s = "Hello World  "
print(lengthOfLastWord(s))