# Primeiro, verificamos se o array já está ordenado; se estiver, não é necessário fazer nenhuma operação. Caso contrário, o algoritmo repete um processo até que o array fique ordenado. Em cada iteração, percorremos o array para encontrar o par de elementos adjacentes com a menor soma. Esse par é então “fundido”: removemos um dos elementos e substituímos o outro pela soma dos dois. Cada fusão conta como uma operação. Repetimos esse processo, reduzindo o tamanho do array e alterando seus valores, até que ele fique totalmente ordenado. O resultado final é o número de fusões necessárias para alcançar a ordenação.

from typing import List

def minimumPairRemoval(nums: List[int]) -> int:
    if nums == sorted(nums):
        return 0

    count = 0

    while nums != sorted(nums):
        min = nums[0] + nums[1]
        index = -1
        for x in range(1, len(nums)-1):
            curSum = nums[x] + nums[x+1]
            if min > curSum:
                min = curSum
                index = x

        nums.pop(index)
        nums[index] = min
        count += 1

    return count


nums = [2, 2, -1, 3, -2, 2, 1, 1, 1, 0, -1]
print(minimumPairRemoval(nums))  # Example usage
