# A ideia do problema é encontrar o menor número formado apenas por 1s (tipo 1, 11, 111...) que seja divisível por k, mas sem construir esse número de fato, já que ele pode ficar gigante. Em vez disso, a solução usa apenas o resto da divisão por k, simulando a construção do número passo a passo com a fórmula (resto * 10 + 1) % k. A cada iteração, isso representa adicionar um novo 1 ao final do número. Quando o resto vira 0, significa que encontramos um número divisível por k, e o tamanho desse número é a resposta. Se k for múltiplo de 2 ou 5, é impossível existir tal número, então retornamos -1. Além disso, como existem no máximo k restos diferentes, usamos isso como limite para evitar loop infinito.

def smallestRepunitDivByK(self, k: int) -> int:
    
    if k % 2 == 0 or k % 5 == 0:
        return -1

    remainder = 0
    for length in range(1, k + 1):
        remainder = (remainder * 10 + 1) % k
        if remainder == 0:
            return length

    return -1


k = 701
print(smallestRepunitDivByK(None, k))