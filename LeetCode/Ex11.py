def maxArea(height):
    """
    output = 0

    for x in range(len(height)):
        if x+1 != len(height) and height[x] < height[x+1]:
            continue
        else:
            for y in range(0, x):
                output = max(output, min(height[y],height[x]) * (x-y))

    return output
    """
    x, y = 0, len(height) - 1
    output = 0

    while x != y:
        output = max(output, min(height[y], height[x]) * (y-x))

        if height[x] > height[y]:
            y -= 1
        else:
            x += 1
    return output

height = [1, 8, 6, 2,5,4,8,3,7]
print(maxArea(height))
