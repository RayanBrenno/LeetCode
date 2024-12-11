def isHappy(n):
    repeated = []
    while True:
        n = sum(int(x)**2 for x in str(n))
        if n in repeated:
            break
        repeated.append(n)
        
    return n


n = 19
print(isHappy(n))
