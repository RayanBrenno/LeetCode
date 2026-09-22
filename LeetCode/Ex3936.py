# A implementação utiliza dois ponteiros, `left` começando no início e `right` no final do array, para encontrar um `0` à esquerda e um elemento diferente de `0` à direita. Quando esses dois elementos são encontrados, eles são trocados, aumentando `ans`, que representa a quantidade mínima de trocas. Após cada troca, os ponteiros avançam para continuar procurando os próximos elementos que precisam ser movidos, até que se encontrem.


from typing import List


def minimumSwaps(self, nums: List[int]) -> int:
    ans = 0
    left, right = 0, len(nums) - 1

    while left < right:
        while left < right and nums[left] != 0:
            left += 1

        while left < right and nums[right] == 0:
            right -= 1

        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
            ans += 1
            left += 1
            right -= 1

    return ans


nums = [0, 1, 0, 3, 12]
print(minimumSwaps(nums))  # Saída: 2