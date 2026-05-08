# O exercício pede para encontrar o menor múltiplo positivo de k que falta na lista. A ideia é verificar sequencialmente 1*k, 2*k, 3*k e assim por diante até encontrar um valor que não está na lista e retorná-lo. Para tornar as buscas rápidas, converte-se a lista para um conjunto (set) no início, permitindo verificações O(1) em vez de O(n) por elemento. Assim o algoritmo completo fica O(n) em vez de O(n²).

from typing import List

def missingMultiple(self, nums: List[int], k: int) -> int:
    num_set = set(nums)
    x = 1
    while x * k in num_set:
        x += 1
    return x * k


nums = [1, 2, 3, 4, 5]
k = 2
print(missingMultiple(None, nums, k))  # Output: 12