# A função converte a letra da coordenada para um número de coluna usando ord(), transforma o número da linha em inteiro e soma os dois valores. Se essa soma for ímpar, significa que a casa do tabuleiro é branca, retornando True; caso contrário, retorna False.

def squareIsWhite(self, coordinates: str) -> bool:
    col = ord(coordinates[0]) - ord("a") + 1
    row = int(coordinates[1])
    print(col + row)
    return True if (col + row) % 2 == 1 else False


coordinates = "a1"
print(squareIsWhite(None, coordinates))
