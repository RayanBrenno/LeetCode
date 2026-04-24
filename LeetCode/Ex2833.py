# A função resolve o problema de forma direta ao contar quantas vezes cada tipo de movimento aparece na string: ela calcula a diferença entre a quantidade de passos para a direita ('R') e para a esquerda ('L'), usando valor absoluto para obter o deslocamento já fixo, e depois soma a quantidade de movimentos flexíveis ('_'), já que todos eles podem ser escolhidos na direção que maximize essa distância; assim, o resultado final representa o ponto mais distante possível da origem considerando a melhor escolha global para os '_'.

def furthestDistanceFromOrigin(self, moves: str) -> int:
    return abs(moves.count("R") - moves.count("L")) + moves.count("_")


moves = "L_RL__R"
print(furthestDistanceFromOrigin(None, moves))