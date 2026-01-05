from typing import List


def finalPrices(prices: List[int]) -> List[int]:

    stack = []
    result = [x for x in prices]
    for x in range(len(prices)):
        while stack and prices[stack[-1]] >= prices[x]:
            index = stack.pop()
            result[index] = prices[index] - prices[x]
        stack.append(x)
    return result


prices = [8, 9, 9, 9, 9]
[1, 3, 2, 1, 7, 0, 6, 6, 9, 1]
[1, 3, 2, 1, 7, 0, 0, 6, 9, 1]
print(finalPrices(prices))
