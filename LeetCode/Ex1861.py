# O código simula a “gravidade” nas pedras (#) dentro de cada linha da caixa, fazendo com que elas caiam para a direita até encontrar um obstáculo (*) ou outra pedra. Para isso, ele percorre cada linha de trás para frente usando um ponteiro (aux) que indica a posição mais à direita onde uma pedra pode cair; quando encontra uma pedra e essa posição está vazia (.), ele troca os elementos e move o ponteiro. Sempre que encontra um obstáculo ou uma pedra fixa, o ponteiro é reajustado para a esquerda, limitando a queda. Depois de processar todas as linhas, ele rotaciona a matriz 90° no sentido horário usando zip com a lista invertida, retornando a caixa já com as pedras “caídas” e rotacionada.

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


box = [["#","#","*",".","*",".",'.'],
       ["#","#","#","*",".",".",'.'],
       ["#","#","#",".",'.',"#","."]]
print(rotateTheBox(box))
