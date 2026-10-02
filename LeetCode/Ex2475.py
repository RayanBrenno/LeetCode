# A implementação utiliza um `Counter` para contar quantas vezes cada valor aparece no array e, em seguida, percorre cada grupo de valores diferentes, usando `aux` para representar a quantidade de elementos dos grupos anteriores. Para cada grupo atual, a multiplicação entre `aux`, a frequência do valor atual e a quantidade de elementos restantes calcula quantos triplets podem ser formados escolhendo um elemento de cada grupo, garantindo que os três valores sejam diferentes. Por fim, essas quantidades são acumuladas em `ans` e retornadas.


from typing import Counter


def unequalTriplets(self, nums: list[int]) -> int:
    count = Counter(nums)

    ans = 0
    aux = 0

    for x in count:
        ans += aux * count[x] * (len(nums) - aux - count[x])
        aux += count[x]

    return ans


nums = [4, 4, 2, 4, 3]
print(unequalTriplets(None, nums))