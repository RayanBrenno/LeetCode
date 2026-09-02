# A implementação retorna diretamente True, pois é sempre possível construir nums2 com todos os elementos tendo a mesma paridade, escolhendo para cada posição manter o próprio valor ou subtrair outro elemento de nums1 quando necessário.

def uniformArray(self, nums1: list[int]) -> bool:
    return True


nums1 = [1, 2, 3, 4]
print(uniformArray(None, nums1))  # Output: True