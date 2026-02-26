# Enquanto o número for maior que 0, ele aplica a regra do problema — se for par, divide por 2; se for ímpar, subtrai 1 — contando cada operação. Ele usa uma expressão condicional numa linha só para decidir a operação, soma 1 ao contador a cada passo e continua até o número virar 0. Basicamente, é uma simulação simples e enxuta do processo até zerar o valor.

def numberOfSteps(self, num: int) -> int:
    ans = 0
    while num > 0:
        num = num//2 if num % 2 == 0 else num-1
        ans += 1
    return ans


num = 14
print(numberOfSteps(None, num))