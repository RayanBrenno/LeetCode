from collections import defaultdict


def maxEqualRowsAfterFlips(matrix):

    res = defaultdict(int)
    
    for row in matrix:
        aux = tuple(row)
        if row[0] == 1:
            aux = tuple([0 if x == 1 else 1 for x in row])
        res[aux] +=1
        
    return max(res.values())


matrix = [[0, 0, 0], [0, 0, 1], [1, 1, 0]]
print(maxEqualRowsAfterFlips(matrix))
