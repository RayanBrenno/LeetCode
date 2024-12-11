def countUnguarded(m, n, guards, walls):
    tab = [[0] * n for x in range(m)]

    for i, j in guards:
        tab[i][j] = 'G'
    for i, j in walls:
        tab[i][j] = 'W'

    def guarded(i, j):
        # row for right
        for row in range(j+1, n):
            if tab[i][row] in ['G', 'W']:
                break
            tab[i][row] = 'S'
        # row for left
        for row in range(j-1,-1,-1):
            if tab[i][row] in ['G', 'W']:
                break
            tab[i][row] = 'S'
        # colloum down
        for col in range(i+1,m):
            if tab[col][j] in ['G', 'W']:
                break
            tab[col][j] = 'S'
        # colloum up
        for col in range(i-1,-1,-1):
            if tab[col][j] in ['G', 'W']:
                break
            tab[col][j] = 'S'

    for i, j in guards:
        guarded(i, j)

    res = 0
    
    for row in tab:
        for char in row:
            if char == 0:
                res += 1
    return res


m = 4
n = 6
guards = [[0, 0], [1, 1], [2, 3]]
walls = [[0, 1], [2, 2], [1, 4]]
print(countUnguarded(m, n, guards, walls))
