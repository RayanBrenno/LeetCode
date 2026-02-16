def isSameAfterReversals(self, num: int) -> bool:
    if num == 0:
        return True
    num_str = str(num)
    return num_str[-1] != '0'    
    
    # return num % 10 != 0

num = 0
print(isSameAfterReversals(None, num))
num = 526
print(isSameAfterReversals(None, num))
num = 1800
print(isSameAfterReversals(None, num))


print(32555% 10**3)