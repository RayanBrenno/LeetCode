# A solução utiliza sliding window com dois ponteiros para encontrar o maior subarray em que nenhum número aparece mais de k vezes. O counter armazena a frequência dos elementos dentro da janela, enquanto start representa a posição anterior ao início dela. A cada elemento percorrido, sua frequência é incrementada e, caso ultrapasse k, o início da janela avança até que a frequência volte a ser válida, removendo os elementos que ficaram para trás do contador. Em seguida, ans é atualizado com o maior tamanho de janela encontrado. Assim, cada elemento é adicionado e removido da janela no máximo uma vez, resultando em O(n) de tempo e O(n) de espaço.

from collections import defaultdict
from typing import List

def maxSubarrayLength(self, nums: List[int], k: int) -> int:
    ans = 0
    start = -1
    counter = defaultdict(int)
    for x in range(len(nums)):
        counter[nums[x]] += 1
        while counter[nums[x]] > k:
            start += 1
            counter[nums[start]] -= 1
        ans = max(ans, x-start)
        print(f"start: {start}, x: {x}, counter: {counter}, ans: {ans}")

    return ans


nums = [1,4,4,3]
k = 1
print(maxSubarrayLength(None, nums, k))

