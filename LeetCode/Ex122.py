def maxProfit(prices):
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]

    return profit

    """
    
    for index, value in enumerate(prices):
        if bolIgnoreOne: bolIgnoreOne = True
        
        if value < buy:
            print(profit)
            buy = value
            aux = 0
            for x in range(index +1, len(prices)):
                aux = max(aux, prices[x]-buy)
            profit += aux
            buy = float('inf')
            bolIgnoreOne = True
        else:
            profit += max(profit, x-buy)

    return profit
    """


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))
