# A implementação utiliza dois dicionários para armazenar a correspondência entre os caracteres das duas strings, verificando cada posição simultaneamente. Um dicionário garante que cada caractere de s sempre corresponda ao mesmo caractere de t, enquanto o outro garante que essa relação seja única, impedindo que caracteres diferentes sejam associados ao mesmo caractere. Caso alguma correspondência seja inconsistente, retorna False; se todas forem válidas, retorna True.


from collections import defaultdict


def isIsomorphic(self, s: str, t: str) -> bool:
    sCount = defaultdict(str)
    tCount = defaultdict(str)

    for x in range(len(s)):
        if s[x] in sCount and sCount[s[x]] != t[x]:
            return False

        if t[x] in tCount and tCount[t[x]] != s[x]:
            return False

        sCount[s[x]] = t[x]
        tCount[t[x]] = s[x]

    return True


s = "egg"
t = "add"
print(isIsomorphic(None, s, t))
