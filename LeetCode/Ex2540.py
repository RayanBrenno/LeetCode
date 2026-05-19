# O exercício pede o primeiro elemento comum entre duas listas ordenadas. A solução usa dois ponteiros, um em cada lista, avançando o que tiver o menor valor até encontrar um elemento igual nos dois — retornando ele imediatamente. Tem uma checagem inicial que descarta o caso onde os ranges das listas nem se cruzam, evitando o loop inteiro.

from typing import List

def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
    if nums1[-1] < nums2[0] or nums2[-1] < nums1[0]:
        return -1

    x1, x2 = 0, 0
    n1, n2 = len(nums1), len(nums2)
    while x1 < n1 and x2 < n2:
        if nums1[x1] == nums2[x2]:
            return nums1[x1]

        elif nums1[x1] < nums2[x2]:
            x1 += 1

        else:
            x2 += 1

    return -1
