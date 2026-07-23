# Primeiro ordenamos o array para facilitar a escolha de onde dividir os elementos. Inicialmente, consideramos como resposta a diferença entre o maior e o menor valor, correspondente ao caso em que todos recebem a mesma operação (+k ou -k). Em seguida, testamos cada possível ponto de divisão, assumindo que todos os elementos à esquerda recebem +k e todos os da direita recebem -k. Para cada divisão, calculamos o novo maior valor (max(nums[i] + k, nums[-1] - k)) e o novo menor valor (min(nums[0] + k, nums[i + 1] - k)), obtendo a diferença entre eles. Mantemos a menor diferença encontrada ao longo de todas as divisões e, ao final, retornamos esse menor intervalo possível.

from typing import List

def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = nums[-1] - nums[0]  # caso base: todos com o mesmo sinal

        for i in range(len(nums) - 1):
            # nums[:i+1] recebe +k, nums[i+1:] recebe -k
            maxA = max(nums[i] + k, nums[-1] - k)
            minA = min(nums[0] + k, nums[i + 1] - k)
            ans = min(ans, maxA - minA)

        return ans
    
    
nums = [1, 3, 6]
k = 3
print(smallestRangeII(None, nums, k))