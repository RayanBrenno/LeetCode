def reverse(x):

    aux = str(x)[::-1]

    x = int(aux) if aux[len(aux)-1] != "-" else -int(aux[0:-1])

    return x if -2**31 < x < 2**31-1 else 0


x = 1534236469
print(reverse(x))
x = -123
print(reverse(x))
