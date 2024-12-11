def numRookCaptures(board):
    def canAttack(i, j):
        res = 0
        for row in range(j+1, len(board[i])):
            if board[i][row] == "B":
                break
            if board[i][row] == "p":
                res += 1
                break
        for row in range(j-1, -1, -1):
            if board[i][row] == "B":
                break
            if board[i][row] == "p":
                res += 1
                break
        for col in range(i+1, len(board)):
            if board[col][j] == "B":
                break
            if board[col][j] == "p":
                res += 1
                break
        for col in range(i-1, -1, -1):
            if board[col][j] == "B":
                break
            if board[col][j] == "p":
                res += 1
                break
        return res

    for i in range(len(board)):
        if "R" in board[i]:
            j = board[i].index("R")
            res = canAttack(i, j)
            return res
    return 0


board = [[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."], ["p", "p", ".", "R", ".", "p", "B", "."], [
    ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "B", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]

print(numRookCaptures(board))
