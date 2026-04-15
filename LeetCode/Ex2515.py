# A função duplica parcialmente a lista de palavras para simular o comportamento circular, permitindo buscar o alvo tanto para frente quanto “dando a volta”. Em seguida, percorre todos os índices e, sempre que encontra a palavra igual ao target, calcula a menor distância até o startIndex, considerando tanto o caminho direto quanto o circular. Durante esse processo, mantém o menor valor encontrado e, ao final, retorna essa menor distância; caso o alvo não seja encontrado, retorna -1.

from typing import List


def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
    words = words + words[0:startIndex]
    n = len(words)
    ans = float('inf')
    for x in range(startIndex, n):
        if words[x] == target:
            ans = min(ans, x - startIndex, n - x)

    return ans if ans != float('inf') else -1


words = ["hello", "i", "am", "leetcode", "hello"]
target = "hello"
startIndex = 1
print(closestTarget(None, words, target, startIndex))
