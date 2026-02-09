def minBitFlips(self, start: int, goal: int) -> int:
    count = 0

    while start > 0 or goal > 0:
        if (start & 1) != (goal & 1):
            count += 1
        start >>= 1
        goal >>= 1

    return count


start = 10
goal = 7
print(minBitFlips(None, start, goal))
