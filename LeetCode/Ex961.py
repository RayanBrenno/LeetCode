# A ideia do algoritmo é aproveitar o fato de que o array possui tamanho 2N e apenas um elemento se repete exatamente N vezes, enquanto todos os outros aparecem apenas uma vez. Devido a essa alta frequência, não é possível espalhar esse elemento repetido pelo array sem que pelo menos duas de suas ocorrências fiquem muito próximas.
# Assim, ao percorrer o array, basta verificar se um elemento é igual ao próximo (i + 1) ou ao elemento duas posições à frente (i + 2). Se isso acontecer, temos certeza de que esse é o valor que se repete N vezes, pois os demais elementos aparecem apenas uma única vez e não satisfazem essa condição.
# Além disso, é feita uma verificação extra entre o primeiro e o último elemento do array para cobrir casos em que o número repetido aparece nas extremidades. Dessa forma, o algoritmo encontra a resposta em uma única passagem pelo array, com complexidade O(n) e uso constante de memória.
from typing import List
def repeatedNTimes(nums: List[int]) -> int:
    n = len(nums) - 1
    if nums[0] == nums[n]:
        return nums[0]
    for i in range(n):
        if nums[i] == nums[i + 1] or nums[i] == nums[i + 2]:
            return nums[i]
    return nums[0]

nums = [1,2,3,4,3,3]
print(repeatedNTimes(nums))

