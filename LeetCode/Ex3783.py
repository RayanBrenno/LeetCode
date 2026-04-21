# A função recebe um número inteiro, transforma esse número em string para inverter a ordem dos seus dígitos, converte o resultado de volta para inteiro e então calcula a diferença absoluta entre o número original e o número invertido, retornando essa distância como resultado.

def mirrorDistance(self, n: int) -> int:
    return abs(n - int(str(n)[::-1]))


n = 123
print(mirrorDistance(None, n))