from collections import Counter


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    else:
        for x in s:
            auxS = s.count(x)
            auxT = s.count(x)
            print(auxT, auxT)
            if auxS != auxT:
                return False

    return True

    """
    return Counter(s) == Counter(t)
    """


s = "rat"
t = "car"
print(isAnagram(s, t))
