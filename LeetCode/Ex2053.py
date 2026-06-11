# A ideia é contar quantas vezes cada string aparece e depois percorrer o array na ordem original, pegando apenas as que aparecem uma única vez. Quando encontrar a k-ésima string distinta, retorna ela.

from collections import Counter
from typing import List

def kthDistinct(self, arr: List[str], k: int) -> str:
    count = Counter(arr)
    print(count)
    for x in (count):
        if count[x] == 1:
            k -= 1
            if k == 0:
                return x

    return ""


arr = ["d","b","c","b","c","a"]
k = 2
print(kthDistinct(None, arr, k))  # Output: "a"