# A solução aproveita uma propriedade da operação XOR e o fato de que `nums` é uma permutação dos números de `1` até `n`. Quando dois dos três índices são iguais, o XOR se reduz ao terceiro valor (`a ^ a ^ b = b`), garantindo que todos os números do vetor já fazem parte da resposta. Para `n < 3`, não é possível formar um trio com três valores distintos, então a quantidade de resultados únicos é simplesmente `n`. Já para `n >= 3`, existe a propriedade de que é possível obter todos os valores no intervalo de `0` até `2^k - 1`, onde `k` é a quantidade de bits necessária para representar `n` (`n.bit_length()`). Assim, basta retornar `2^k`, calculado de forma eficiente com `1 << n.bit_length()`, obtendo a resposta em tempo constante e sem utilizar estruturas auxiliares.


from typing import List


def uniqueXorTriplets(self, nums: List[int]) -> int:
    n = len(nums)

    if n < 3:
        return n

    return 1 << n.bit_length()


nums = [1, 2, 3]
print(uniqueXorTriplets(None, nums))
