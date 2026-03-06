# Esse exercício verifica se o maior segmento contínuo de 1s é maior que o maior segmento contínuo de 0s. A solução usa split() para quebrar a string: s.split("0") separa a string onde aparecem 0s, deixando apenas os blocos de 1s, e max() pega o maior bloco de 1s. Da mesma forma, s.split("1") cria os blocos de 0s e max() pega o maior deles. No final, o código compara o tamanho desses dois blocos com len() e retorna True se o maior bloco de 1s for maior que o maior bloco de 0s, caso contrário retorna False.

def checkZeroOnes(self, s: str) -> bool:
    # one = s.split("0")
    # zeros = s.split("1")
    # return len(max(one)) > len(max(zeros))
    return len(max(s.split("0"))) > len(max(s.split("1")))


s = "1101"
print(checkZeroOnes(None, s))