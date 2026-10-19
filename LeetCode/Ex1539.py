# A implementação percorre os números a partir de 1 usando count e verifica se cada número corresponde ao próximo elemento de arr, utilizando x para avançar pelo array ordenado sem precisar procurar em todas as posições. Quando o número não está presente, decrementa k, até encontrar o k-ésimo número positivo ausente, que é retornado em count.


def findKthPositive(self, arr: list[int], k: int) -> int:
    count = 0
    x = 0

    while k > 0:
        count += 1
        if x < len(arr) and count == arr[x]:
            x += 1
        else:
            k -= 1

    return count

    # count = 0
    # while k > 0:
    #     count += 1
    #     if count not in arr:
    #         k -= 1
    # return count


arr = [2, 3, 4, 7, 11]
k = 5
print(findKthPositive(None, arr, k))
