# A implementação percorre os números a partir de n até encontrar o primeiro cujo produto dos dígitos seja divisível por t. Para cada candidato, inicializa uma variável com 1, percorre todos os seus dígitos convertendo o número para string e multiplica cada dígito ao produto acumulado. Ao final, verifica se esse produto é divisível por t; se for, retorna imediatamente o número, garantindo que ele seja o menor possível. Caso contrário, incrementa n e repete o processo até encontrar uma resposta válida.

def smallestNumber(self, n: int, t: int) -> int:
    while True:
        aux = 1

        for x in str(n):
            aux *= int(x)

        if aux % t == 0:
            return n

        n += 1


n = 1656
t = 6
print(smallestNumber(None, n, t))
