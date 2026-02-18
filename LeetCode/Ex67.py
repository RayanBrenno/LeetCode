# Esse código soma duas strings que representam números binários. Ele começa pelos últimos dígitos de cada string (da direita para a esquerda), usando dois ponteiros, e mantém uma variável carry para guardar o vai-um da soma. A cada passo, soma os bits atuais de a e b ao carry, coloca no início da string resultado o resto da divisão por 2 (carry % 2), que é o bit correto daquela posição, e atualiza o carry dividindo por 2. O loop continua enquanto ainda houver dígitos para processar ou existir vai-um pendente. No final, retorna a string com a soma binária completa.

def addBinary(a, b):
    output = ''
    carry = 0
    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 or j >= 0 or carry:
        if i >= 0:
            carry += int(a[i])
            i -= 1
        if j >= 0:
            carry += int(b[j])
            j -= 1
        output = str(carry % 2) + output
        carry = carry // 2

    return output

a = "11"
b = "1"
print(addBinary(a, b))