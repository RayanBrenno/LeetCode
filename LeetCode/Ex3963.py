# A ideia é criar a primeira linha completamente livre, usando "." * n, permitindo avançar até a última coluna. Para as demais linhas, são colocados obstáculos nas primeiras n - 1 colunas e uma célula livre na última coluna, garantindo que o único caminho possível seja seguir pela primeira linha e depois descer pela última coluna até o destino.

def createGrid(self, m: int, n: int) -> list[str]:
    return ["." * n] + ["#" * (n-1) + "."] * (m - 1)


m = 4
n = 5
print(createGrid(None, m, n))  # Output: ['.....', '####.', '####.', '####.']
