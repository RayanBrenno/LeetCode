def climbStairs(n: int) -> int:
    res = []
    for x in range(1, n+1):
        if len(res) < 2:
            res.append(x)
        else:
            res.append(res[-1] + res[-2])
    return res[-1]


n = 40
print(climbStairs(n))
