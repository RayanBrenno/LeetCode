def rotateTheBox(box):
    newBox = []
    for row in box:
        aux = len(row) - 1
        for x in range(len(row)-1, -1, -1):
            if row[x] == "#" and row[aux] == ".":
                row[aux], row[x] = row[x], row[aux]
                aux -= 1

            if row[x] == "*" or row[x] == "#":
                aux = x - 1

        newBox.append(row)

    rotatedBox = zip(*newBox[::-1])
    return rotatedBox


box = [["#", "#", "*", ".", "*", "."],
       ["#", "#", "#", "*", ".", "."],
       ["#", ".", ".", "*", "#", "."]]
print(rotateTheBox(box))
