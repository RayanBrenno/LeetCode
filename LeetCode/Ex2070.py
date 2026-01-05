def maximumBeauty(items, queries):

    items = sorted(items, key=lambda x: x[1], reverse=True)
    output = []
    for x in queries:
        max = 0
        for y in items:
            print(y)
            if y[0] <= x:
                print("entro")
                max = y[1]
                break

        output.append(max)

    return output

    """
    items = sorted(items, key=lambda x:x[0])
    output = []
    for x in queries:
        max = 0
        for y in range(len(items)):
            if items[y][0] > x:
                break
            if items[y][1] > max:
                max = items[y][1]

        output.append(max)

    return 0 if len(output) == 0 else output
    """


items = [[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]]
queries = [1, 2, 3, 4, 5, 6]
print(maximumBeauty(items, queries))
