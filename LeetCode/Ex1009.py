#O complemento de um número pode ser obtido invertendo todos os bits até o bit mais significativo. Para isso, criamos uma máscara de 1s com o mesmo número de bits usando (1 << n.bit_length()) - 1 e fazemos XOR com n, pois 1 ^ 0 = 1 e 1 ^ 1 = 0, invertendo os bits.

def bitwiseComplement(self, n: int) -> int:
    if n == 0:
        return 1
    mask = (1 << n.bit_length()) - 1
    return n ^ mask

n = 5
print(bitwiseComplement(None, n))