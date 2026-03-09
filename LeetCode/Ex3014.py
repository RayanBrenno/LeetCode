# A ideia do exercício é minimizar o número de vezes que as teclas são pressionadas para escrever a palavra. Como existem 8 teclas disponíveis (2–9), podemos colocar até 8 letras na primeira posição das teclas, que custam 1 push, as próximas 8 letras na segunda posição, que custam 2 pushes, e assim por diante. Para minimizar o total, primeiro contamos a frequência de cada letra na palavra, depois ordenamos da maior para a menor, pois as letras que aparecem mais vezes devem ficar nas posições que exigem menos pushes. Em seguida percorremos essas frequências e calculamos o custo usando pushes = i // 8 + 1, somando frequência * pushes para obter o total mínimo de pressões necessárias

from collections import Counter


def minimumPushes(self, word: str) -> int:
    count = sorted(Counter(word).values(), reverse=True)

    ans = 0
    for i, f in enumerate(count):
        pushes = (i // 8) + 1
        
        ans += f * pushes
        print(i,f, "pushes:", pushes, "ans:", ans)

    return ans


word = "xycdefghij"
print(minimumPushes(None, word))