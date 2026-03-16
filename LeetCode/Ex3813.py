# Percorremos a string s contando quantas vogais e consoantes existem. Para isso usamos sum(x in v for x in s) para contar as vogais (aeiou) e o mesmo processo para contar as consoantes. Depois verificamos se existe apenas um dos tipos de letra na string; se não houver vogais ou não houver consoantes, retornamos 0, pois não é possível calcular a razão entre elas. Caso existam ambos, retornamos o score calculado pela divisão inteira entre o número de vogais e o número de consoantes (count_v // count_c).

def vowelConsonantScore(self, s: str) -> int:
    v = "aeiou"
    count_v = sum(x in v for x in s)
    c = "bcdfghjklmnpqrstvwxyz"
    count_c = sum(x in c for x in s)

    if count_c == 0 or count_v == 0:
        return 0

    return count_v // count_c


s = "aeiou"
print(vowelConsonantScore(s))
s = "leetcode"
print(vowelConsonantScore(s))