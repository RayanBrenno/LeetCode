def isValidSudoku(board):
    
    for x in range(len(board)):
        
        unique = []
        for y in board[x]:
            if y not in unique:
                unique.append(y)
            elif y in unique and y != ".":
                return False

        cont = 0
        unique = []
        while cont < 9:
            if board[cont][x] not in unique:
                unique.append(board[cont][x])
            elif board[cont][x] in unique and board[cont][x] != ".":
                return False
            cont += 1
            
            
    unique = []
    cont = 0 
    for time in range(3):
        for x in range(9):
            if x%3 == 0:
                unique = []
                cont = time*3
            while cont < (time+1)*3:
                if board[x][cont] not in unique:
                    unique.append(board[x][cont])
                elif board[x][cont] in unique and board[x][cont] != ".":
                    return False
                cont +=1
                
            cont = time*3
    
    return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", ""],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(isValidSudoku(board))
