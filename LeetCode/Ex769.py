from typing import List


def maxChunksToSorted(arr: List[int]) -> int:

    chunks = 0
    cruMax = -1

    for i, value in enumerate(arr):
        cruMax = max(value, cruMax)

        if cruMax == i:
            chunks += 1

    return chunks


arr = [4, 3, 2, 1, 0]
print(maxChunksToSorted(arr))
