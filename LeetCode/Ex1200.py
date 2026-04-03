# Ordena o array pra garantir que os números mais próximos fiquem lado a lado, aí percorre uma única vez comparando cada elemento com o anterior; quando encontra uma diferença menor que a atual, atualiza o valor mínimo e reinicia a lista de respostas com esse novo par, e quando encontra uma diferença igual à mínima, apenas adiciona o par à lista — assim você resolve tudo em uma passada só de forma eficiente e limpa.

from typing import List

def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
    arr.sort()
    n = len(arr)
    min_dif = float("inf")
    ans = []
    for x in range(1, n):
        diff = arr[x] - arr[x - 1]

        if diff < min_dif:
            min_dif = diff
            ans = [[arr[x - 1], arr[x]]]

        elif diff == min_dif:
            ans.append([arr[x - 1], arr[x]])

    return ans


arr = [4, 2, 1, 3]
print(minimumAbsDifference(None, arr))