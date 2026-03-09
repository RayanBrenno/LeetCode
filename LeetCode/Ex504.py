# A ideia do exercício é converter um número inteiro para base 7. Primeiro o código trata casos especiais: se o número for 0, retorna "0". Depois verifica se o número é negativo e guarda o sinal "-" se for. Em seguida transforma o número em positivo com abs(num) e começa a montar a resposta: enquanto num for maior que 0, ele pega o resto da divisão por 7 (num % 7), que representa o próximo dígito na base 7, adiciona esse dígito no início da string ans, e divide o número por 7 (num //= 7) para continuar o processo. No final, ele junta o sinal (se houver) com o resultado e retorna o número convertido para base 7.

def convertToBase7(self, num: int) -> str:
    if num == 0:
        return "0"
    sign = "-" if num < 0 else ""
    ans = ""
    num = abs(num)
    while num:
        ans = str(num % 7) + ans
        num //= 7
    return sign + ans


num = -7
print(convertToBase7(None, num))