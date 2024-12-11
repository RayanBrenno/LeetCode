def myPow(x, n):
    if n == 0:
        return 1
    elif n > 0:
        output = x
        for w in range(1, n):
            output *= x
        return output
    else:
        output = 1 / x
        for w in range(1, abs(n)):
            output /= x
        return output

    """ FUNCIONA
    return x**n
    """


x = 34.00515
n = -3
print(myPow(x, n))
