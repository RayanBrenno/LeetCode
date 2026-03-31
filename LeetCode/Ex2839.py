# A função verifica se duas strings podem ser consideradas iguais ao permitir trocas apenas entre posições específicas: ela separa os caracteres dos índices pares (0 e 2) e dos índices ímpares (1 e 3) de cada string, transformando esses pares em conjuntos. Como conjuntos não se importam com ordem, isso equivale a checar se os mesmos caracteres existem nesses grupos independentemente da posição. No final, retorna True apenas se os caracteres das posições pares de s1 forem iguais aos de s2 e o mesmo acontecer com as posições ímpares, garantindo que uma pode ser transformada na outra usando essas trocas permitidas.

def canBeEqual(self, s1: str, s2: str) -> bool:
    if s1[0].isnumeric():
        print
    return {s1[0], s1[2]} == {s2[0], s2[2]} and {s1[1], s1[3]} == {s2[1], s2[3]}
    

s1 = "abcd"
s2 = "cdab"
print(canBeEqual(None, s1, s2))