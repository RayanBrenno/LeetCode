# A função usa dois ponteiros (i para nums1 e j para nums2) para percorrer os arrays ao mesmo tempo e encontrar a maior distância válida: ela garante que j nunca fique atrás de i, e enquanto nums1[i] <= nums2[j], atualiza a resposta com j - i e avança j para tentar aumentar a distância; quando a condição falha, avança i para buscar um valor menor em nums1, aproveitando o fato de ambos os arrays serem não crescentes para evitar comparações desnecessárias e manter a solução eficiente.

from typing import List

def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
    i = j = 0
    ans = 0
    n1, n2 = len(nums1), len(nums2)

    while i < n1 and j < n2:
        if i > j:
            j = i

        if j < n2 and nums1[i] <= nums2[j]:
            ans = max(ans, j - i)
            j += 1

        else:
            i += 1

    return ans


nums1 = [55, 30, 5, 4, 2]
nums2 = [100, 20, 10, 10, 5]
print(maxDistance(None, nums1, nums2))