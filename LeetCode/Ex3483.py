# A implementação percorre todas as possibilidades de centenas, dezenas e unidades usando os índices dos dígitos para permitir valores repetidos em posições diferentes. O primeiro dígito não pode ser zero e o último precisa ser par. Cada número válido é adicionado a um `set`, evitando duplicatas, e no final é retornada a quantidade de números distintos encontrados.


from typing import List


def totalNumbers(self, digits: List[int]) -> int:
    ans = set()

    for x in range(len(digits)):
        if digits[x] == 0:
            continue

        for y in range(len(digits)):
            for z in range(len(digits)):
                if z != x and z != y and x != y and digits[z] % 2 == 0:
                    ans.add(digits[x] * 100 + digits[y] * 10 + digits[z])

    return len(ans)


digits = [1, 2, 3, 4]
print(totalNumbers(digits))  # Saída: 12