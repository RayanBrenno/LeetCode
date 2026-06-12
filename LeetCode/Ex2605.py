# O código transforma as duas listas em conjuntos para facilitar a busca de elementos em comum. Se existir algum número presente nas duas listas, ele retorna o menor desses números. Caso não haja interseção, encontra o menor valor de cada lista e forma o menor número possível de dois dígitos concatenando o menor deles primeiro e o maior depois.

from typing import List

def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
    intersection = set(nums1) & set(nums2)

    if intersection:
        return min(intersection)

    min_1 = min(nums1)
    min_2 = min(nums2)
    return min(min_1, min_2) * 10 + max(min_1, min_2)


nums1 = [4, 1, 3]
nums2 = [5, 7]
print(minNumber(None, nums1, nums2))  # Output: 15