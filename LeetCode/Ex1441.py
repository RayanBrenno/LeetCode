# Percorremos os números de 1 até n simulando as operações da pilha. Para cada número fazemos um "Push". Se o número for igual ao elemento atual de target, apenas avançamos o ponteiro i para o próximo elemento do target. Caso contrário, significa que esse número não faz parte do target, então fazemos um "Pop" para removê-lo. O processo continua até construirmos todo o target. A complexidade é O(n) no pior caso, percorrendo os números apenas uma vez.

from typing import List


def buildArray(self, target: List[int], n: int) -> List[str]:
    ans = []
    i = 0

    for num in range(1, n+1):
        ans.append("Push")
        if num == target[i]:
            i += 1
            if i == len(target):
                break
        else:
            ans.append("Pop")

    return ans

    # ans = []
    # x = 0

    # for num in target:
    #     while x < num - 1:
    #         ans.append("Push")
    #         ans.append("Pop")
    #         x += 1

    #     ans.append("Push")
    #     x += 1

    # return ans


target = [1, 3]
n = 3
print(buildArray(None, target, n))
