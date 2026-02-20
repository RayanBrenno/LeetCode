def countOperations(self, num1: int, num2: int) -> int:     
    # res = 0
    # while num1*num2 != 0:
    #     if num1 >= num2:
    #         num1 -= num2
    #     else:
    #         num2 -= num1
    #     res += 1
    # return res
    
    ans = 0

    while num1 * num2 != 0:
        if num1 >= num2:
            ans += num1 // num2
            num1 %= num2
        else:
            ans += num2 // num1
            num2 %= num1

    return ans

num1 = 10
num2 = 3
print(countOperations(None, num1, num2))