# A ideia principal foi percorrer os cupons e filtrar apenas os que são válidos, ou seja, estão ativos, pertencem a uma linha de negócio permitida e possuem um código válido. Em seguida, esses cupons são agrupados pela linha de negócio, ordenados alfabeticamente dentro de cada grupo e concatenados na ordem definida das linhas, formando a lista final.
from typing import List


def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
    lines = ["electronics", "grocery", "pharmacy", "restaurant"]
    aux = [[] for x in range(len(lines))]
    for x in range(len(code)):
        if isActive[x]:
            if businessLine[x] in lines:
                if all(c == "_" or c.isalnum() for c in code[x]) and len(code[x]) > 0:
                    aux[lines.index(businessLine[x])].append(code[x])

    ans = []

    for x in aux:
        if len(x) > 0:
            ans.extend(sorted(x))
    return ans


code = ["1OFw", "0MvB"]
businessLine = ["electronics", "pharmacy"]
isActive = [True, True]
print(validateCoupons(None, code, businessLine, isActive))
