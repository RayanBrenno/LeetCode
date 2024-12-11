import math


def minimizedMaximum(n, quantities):

    def checking(aux):
        stores = [math.ceil(x/aux) for x in quantities]
        return sum(stores) <= n

    big = 1000000000
    left, right = 1, max(quantities)

    while left <= right:
        aux = ((right-left)//2)+1

        if checking(aux):
            big = aux
            right = aux - 1

        else:
            left = aux + 1
            
        print(left, right)

    return big


n = 6
quantities = [11, 6]
print(minimizedMaximum(n, quantities))
