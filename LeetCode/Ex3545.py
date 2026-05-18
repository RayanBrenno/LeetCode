# A função conta a frequência de cada caractere na string, ordena essas frequências em ordem crescente e calcula um limite que determina quantos caracteres menos frequentes precisam ser deletados. Se k for maior que a quantidade de caracteres únicos, nenhuma deleção é necessária; caso contrário, o limite é a diferença entre o total de caracteres únicos e k. Por fim, a função retorna a soma das frequências dos caracteres até esse limite, indicando quantos caracteres devem ser removidos da string.

from collections import defaultdict


def minDeletion(self, s: str, k: int) -> int:
    count = defaultdict(int)
    for x in s:
        count[x] += 1

    frequencies = sorted(count.values())
    limit = 0 if k > len(frequencies) else len(frequencies) - k

    return sum(frequencies[:limit])


s = "aaabbbcc"
k = 2
print(minDeletion(s, k))