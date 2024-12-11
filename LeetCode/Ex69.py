import math
def mySqrt(x):

    if x < 4: return 1 if x else 0
    i = 2
    while i*i <=x:
        i+=1
    return i-1

    """ TOPZERA AQUI
    root=math.sqrt(x)
    return int(root)
    """

x = 24
print(mySqrt(x))
