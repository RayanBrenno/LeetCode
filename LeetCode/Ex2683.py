from typing import List


def doesValidArrayExist(derived: List[int]) -> bool:

    aux = 0
    for element in derived:
        aux = aux ^ element
    return aux == 0


derived = [1, 1, 0]
print(doesValidArrayExist(derived))
