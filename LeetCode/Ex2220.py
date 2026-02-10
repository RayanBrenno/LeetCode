# Enquanto ainda existir bit em start ou goal, o código compara sempre do bit menos valioso pro mais valioso, pegando o último bit com & 1, se forem diferentes soma um flip, depois desloca os dois números pra direita com >> pra analisar o próximo bit, e no final o contador indica quantos bits precisam ser trocados pra transformar start em goal.

def minBitFlips(self, start: int, goal: int) -> int:
    count = 0

    while start > 0 or goal > 0:
        if (start & 1) != (goal & 1):
            count += 1
        start >>= 1
        goal >>= 1

    return count


start = 2
goal = 33
print(minBitFlips(None, start, goal))
