def maxProfit(prices):
    profit = 0
    buy = float('inf')

    for x in prices:
        if x < buy:
            buy = x
        else:
            profit = max(profit, x-buy)

    return profit

prices = prices = [7, 6, 4, 3, 1]
print(maxProfit(prices))

