# A implementação percorre o array comparando cada elemento com o anterior, mantendo dois contadores: inc para a sequência estritamente crescente e dec para a estritamente decrescente. Quando a ordem é quebrada ou existem elementos iguais, o contador correspondente é reiniciado em 1. A cada iteração, atualiza res com o maior valor entre os dois contadores, retornando assim o tamanho da maior subarray monotônica encontrada.

from typing import List


def longestMonotonicSubarray(self, nums: List[int]) -> int:
    n = len(nums)
    res = 1
    inc, dec = 1, 1

    for x in range(1, n):
        if nums[x] > nums[x-1]:
            inc += 1
            dec = 1
        elif nums[x] < nums[x-1]:
            inc = 1
            dec += 1
        else:
            inc = dec = 1
        res = max(res, dec, inc)
    return res


nums = [1, 2, 3, 2, 1]
print(longestMonotonicSubarray(None, nums))
