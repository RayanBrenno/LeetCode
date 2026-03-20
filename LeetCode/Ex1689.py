# Esse código resolve o problema observando uma ideia bem simples: como o número n é uma string composta por dígitos de 0 a 9, o maior dígito presente nela determina o número mínimo de “partições” necessárias. Isso porque cada partição representa um número formado apenas por dígitos 0 ou 1, e para construir um dígito maior (como 7, por exemplo), você precisa somar pelo menos 7 desses números. Assim, o código apenas pega o maior caractere da string com max(n) e converte para inteiro, retornando diretamente esse valor como resposta, de forma extremamente eficiente.

def minPartitions(self, n: str) -> int:
    return int(max(n))


n = "32"
print(minPartitions(None, n))