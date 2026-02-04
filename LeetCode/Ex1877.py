# Após o sort, ele usa dois ponteiros, um no início e outro no fim da lista, somando sempre o menor elemento disponível com o maior. A cada iteração, ele atualiza a resposta com o maior valor entre a soma atual e a maior soma já encontrada. Ao avançar o ponteiro da esquerda e recuar o da direita, todos os números são usados exatamente uma vez em pares, garantindo que a maior soma possível entre os pares seja minimizada e corretamente identificada.
from typing import List


def minPairSum(self, nums: List[int]) -> int:
    nums.sort()
    left, right = 0, len(nums) - 1
    ans = 0
    while left < right:
        ans = max(ans, nums[left] + nums[right])
        left += 1
        right -= 1
    return ans


nums = [3, 5, 2, 3]
print(minPairSum(None, nums))  # Example usage
