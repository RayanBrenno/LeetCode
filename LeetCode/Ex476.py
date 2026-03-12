# O complemento de um número pode ser obtido invertendo todos os bits até o bit mais significativo. Para isso, criamos uma máscara de 1s com o mesmo número de bits usando (1 << n.bit_length()) - 1 e fazemos XOR com n, pois 1 ^ 0 = 1 e 1 ^ 1 = 0, invertendo os bits.

def findComplement(self, num: int) -> int:
    return num ^ ((1 << num.bit_length()) - 1) if num != 0 else 1


num = 5
print(findComplement(None, num))
