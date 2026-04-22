# A função percorre cada palavra em queries e tenta encontrar alguma palavra no dictionary que seja parecida com ela. Para isso, compara caractere por caractere entre a query e cada palavra do dicionário, contando quantas posições são diferentes. Se essa diferença for no máximo 2, considera que a palavra é válida, adiciona a query no resultado e interrompe a busca para aquela palavra (indo para a próxima query). No final, retorna a lista com todas as palavras de queries que possuem pelo menos uma correspondente no dicionário com até duas diferenças.

from typing import List

def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
    ans = []
    for query in queries:
        for s in dictionary:
            dis = 0
            for x in range(len(query)):
                if query[x] != s[x]:
                    dis += 1
            if dis <= 2:
                ans.append(query)
                break
    return ans


queries = ["word","note","ants","wood"]
dictionary = ["wood","joke","moat"]
print(twoEditWords(queries, dictionary))
