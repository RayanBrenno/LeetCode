def generateParenthesis(n):

    def bakctracking(openCont, closeCont, string):
        if openCont == n and closeCont == 0 and len(string) == 2*n:
            res.append(string)
        if openCont < n:
            bakctracking(openCont + 1, closeCont+1, string + "(")
        if closeCont > 0:
            bakctracking(openCont, closeCont-1, string + ")")  
    
    res = []
    bakctracking(0, 0, "")
    return res


n = 3
bla = generateParenthesis(n)[::-1]
for x in bla:
    print(x)