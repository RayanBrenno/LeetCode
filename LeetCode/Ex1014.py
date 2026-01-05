from typing import List


def maxScoreSightseeingPair(values: List[int]) -> int:

    res = 0
    curMax = values[0] - 1

    for x in range(1, len(values)):
        res = max(res, values[x] + curMax)
        curMax = max(curMax - 1, values[x] - 1)

    return res


values = [8, 1, 5, 2, 6]
print(maxScoreSightseeingPair(values))
