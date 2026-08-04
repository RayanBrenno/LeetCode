# A solução encontra o menor e o maior valor do array e considera que todos os números entre eles deveriam existir. Para isso, cria um conjunto contendo todos os valores do intervalo [menor, maior) e, em seguida, remove desse conjunto os elementos que já estão presentes em nums utilizando a diferença entre conjuntos. Por fim, converte o resultado para uma lista ordenada, retornando todos os números que estão faltando entre o menor e o maior elemento do array.

from typing import List


def findMissingElements(self, nums: List[int]) -> List[int]:
    small = min(nums)
    large = max(nums)
    aux = set([x for x in range(small, large)])
    return sorted(list(aux - set(nums)))


nums = [1, 2, 4, 6]
print(findMissingElements(None, nums))
