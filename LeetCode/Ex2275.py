def largestCombination(candidates):

    bits = [0] * 30

    for x in candidates:
        binarie = bin(x)[::-1]
        for y in range(len(binarie)):
            if binarie[y] == '1':
                bits[y] += 1

    return max(bits)


candidates = [16, 17, 71, 62, 12, 24, 14, 1, 2]
print(largestCombination(candidates))
