

from typing import List

def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
    n = len(spells)
    m = len(potions)
    pairs = [0] * n
    potions.sort()
    for i in range(n):
        spell = spells[i]
        l, r = 0, m - 1 
        while l <= r:
            mid = l + (r - l) // 2
            product = spell * potions[mid]
            if product >= success:
                r = mid - 1
            else:
                l = mid + 1
        pairs[i] = m - l
    return pairs


spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7
print(successfulPairs(None, spells, potions, success)) 