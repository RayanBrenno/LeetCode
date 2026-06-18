# Ordeno as operações pelo índice para processá-las da esquerda para a direita. Para cada substituição, verifico se o source realmente aparece na posição indicada da string original. Quando a correspondência é válida, adiciono à resposta o trecho entre a última posição processada e o início da substituição, seguido do target. Em seguida, avanço o ponteiro para o final do trecho substituído. Ao final, acrescento a parte restante da string. Dessa forma, todas as substituições são realizadas com base na string original, sem afetar os índices das demais operações.

from typing import List

def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        ans = []
        prev = 0

        for idx, src, tgt in sorted(zip(indices, sources, targets)):
            if s[idx:idx + len(src)] == src:
                ans.append(s[prev:idx])
                ans.append(tgt)
                prev = idx + len(src)

        ans.append(s[prev:])
        return "".join(ans)
    

s = "abcd"
indices = [0, 2]
sources = ["a", "cd"]
targets = ["eee", "ffff"]
print(findReplaceString(None, s, indices, sources, targets))