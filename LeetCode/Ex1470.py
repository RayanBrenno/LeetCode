# O código separa o array em duas partes: a primeira metade (arrX) e a segunda metade (arrY). Depois, percorre as duas listas ao mesmo tempo usando zip, adicionando alternadamente um elemento de cada metade na lista ans. No final, retorna o array embaralhado no formato x1, y1, x2, y2....

from typing import List

def shuffle(self, nums: List[int], n: int) -> List[int]:
    arrX = nums[:n]
    arrY = nums[n:]
    ans = []
    for x, y in zip(arrX, arrY):
        ans.append(x)
        ans.append(y)

    return ans


nums = [2,5,1,3,4,7]
n = 3
print(shuffle(nums, n))