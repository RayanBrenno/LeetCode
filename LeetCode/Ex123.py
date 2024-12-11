def maxProfit(prices):
    if not prices:
        return 0

    firstProfit = [0] * len(prices)
    minPrice = prices[0]

    for i in range(1, len(prices)):
        minPrice = min(minPrice, prices[i])
        firstProfit[i] = max(firstProfit[i - 1], prices[i] - minPrice)

    secondProfit = [0] * len(prices)
    maxPrice = prices[-1]

    for i in range(len(prices) - 2, -1, -1):
        maxPrice = max(maxPrice, prices[i])
        secondProfit[i] = max(secondProfit[i + 1], maxPrice - prices[i])
        
    output = 0
    for i in range(len(prices)):
        output = max(output, firstProfit[i] + secondProfit[i])

    return output
    
    """
    profit = [0]
    cont = 0

    while cont < len(prices):
        aux = 0
        contInte = 0

        for x in range(cont+1, len(prices)):
            if prices[x] <= prices[cont]:
                contInte = 0
                break
            if x+1 < len(prices) and prices[x] > prices[x+1]:
                aux = max(aux, prices[x]-prices[cont])
                contInte += 1
                break
            else:
                aux = max(aux, prices[x]-prices[cont])
                contInte += 1

        cont += contInte + 1
        profit.append(aux)


    profit.sort()
    print(profit)
    return profit[-1] + profit[-2] if len(profit) >=2 else profit[-1]
    """
    
prices = [1,2,4,2,5,7,2,4,9,0]
print(maxProfit(prices))
