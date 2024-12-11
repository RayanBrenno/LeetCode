def maxCount(banned, n, maxSum):
        banned = set(banned)
        count = 0
        totalSum = 0
        for x in range(1, n+1):
            if x in banned :
                continue
            totalSum+= x
            if totalSum > maxSum:
                break 
            count+=1

        return count
    
        """
    res = []
    for x in range(1, n+1):
        if x not in banned and sum(res) + x < maxSum:
            res.append(x)
        if sum(res) + x > maxSum:
            break 
    banned = set(sorted(banned))
    print(banned)

    return len(res)
    """

banned = [12141]
n = 5080
maxSum = 14
print(maxCount(banned, n, maxSum))
