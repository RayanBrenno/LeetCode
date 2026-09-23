# A implementação usa um `Counter` para acumular a quantidade de visitas de cada domínio e de seus subdomínios. Para cada entrada, separa a quantidade do domínio, adiciona a quantidade ao domínio completo e, usando dois `while`, percorre o domínio procurando os pontos (`.`) para extrair e contabilizar cada subdomínio restante. No final, transforma o `Counter` em uma lista de strings no formato `quantidade domínio`.

from typing import List
import collections


def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
    count = collections.Counter()
    for domain in cpdomains:
        qtd, domain = domain.split()
        qtd = int(qtd)
        count[domain] += qtd
        # domain_splited = domain.split(".")
        x, n = 0, len(domain)

        while x < n:
            aux = x
            while aux < n and domain[aux] != ".":
                aux += 1
            if aux < n:
                count[domain[aux+1:]] += qtd
            x = aux + 1

        # for x in range(len(domain_splited)):
        #     count[".".join(domain_splited[x:])] += qtd

    return [f"{qtd} {domain}" for domain, qtd in count.items()]


cpdomains = ["9001 discuss.leetcode.com","50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
# Saída: ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com", "50 yahoo.com", "50 com", "1 intel.mail.com", "1 mail.com", "1 com", "5 wiki.org", "5 org"]
print(subdomainVisits(cpdomains))
