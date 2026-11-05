# A implementação ordena arr2 e utiliza busca binária para verificar, para cada elemento x de arr1, se existe algum elemento em arr2 cuja diferença absoluta seja menor ou igual a d. Inicialmente, ans recebe o tamanho de arr1 e, sempre que a busca encontra um elemento dentro da distância permitida, decrementa ans e interrompe a busca para aquele elemento. Como arr2 está ordenado, a busca binária consegue descartar metade dos elementos a cada iteração, retornando ao final a quantidade de elementos de arr1 que não possuem nenhum elemento próximo em arr2.

from typing import List


def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
    arr2.sort()
    ans = len(arr1)

    for x in arr1:
        left, right = 0, len(arr2) - 1

        while left <= right:
            mid = (left + right) // 2

            if abs(x - arr2[mid]) <= d:
                ans -= 1
                break

            if arr2[mid] < x - d:
                left = mid + 1
            else:
                right = mid - 1

    return ans


arr1 = [4, 5, 8]
arr2 = [10, 9, 1, 8]
d = 2
print(findTheDistanceValue(None, arr1, arr2, d))