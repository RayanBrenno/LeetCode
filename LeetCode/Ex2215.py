# A ideia é transformar os dois arrays em conjuntos (set), eliminando automaticamente os elementos repetidos. Em seguida, basta calcular a diferença entre os conjuntos: set1 - set2 retorna todos os valores que aparecem apenas em nums1, enquanto set2 - set1 retorna os que aparecem apenas em nums2. Por fim, os resultados são convertidos para listas e retornados na resposta. Assim, a solução é simples e eficiente, aproveitando as operações de diferença entre conjuntos.

from typing import List

def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
    set1 = set(nums1)
    set2 = set(nums2)
    return [list(set1-set2), list(set2-set1)]


nums1 = [1,2,3]
nums2 = [2,4,6]
print(findDifference(None, nums1, nums2))