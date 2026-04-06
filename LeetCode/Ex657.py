# A ideia é verificar se o robô voltou para a posição inicial após executar todos os movimentos. Para isso, basta garantir que os movimentos horizontais se anulam (L = R) e os verticais também (U = D). Se a quantidade de esquerda for igual à de direita e a de cima igual à de baixo, então ele termina no ponto de origem, retornando True; caso contrário, False.

from collections import Counter

def judgeCircle(self, moves: str) -> bool:
    
    return moves.count("L") == moves.count("R") and moves.count("U") == moves.count("D")

    # count = Counter(moves)
    # horizontal = 0
    # vertical = 0
    # if 'L' in count:
    #     horizontal -= count['L']
    # if 'R' in count:
    #     horizontal += count['R']
    # if 'U' in count:
    #     vertical += count['U']
    # if 'D' in count:
    #     vertical -= count['D']
    
    # return horizontal == 0 and vertical == 0


moves = "UD"
print(judgeCircle(None, moves))