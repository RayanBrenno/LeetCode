# A função primeiro ordena a lista de asteroides em ordem crescente para garantir que os menores sejam enfrentados primeiro. Em seguida, percorre cada asteroide verificando se a massa atual é suficiente para destruí-lo; caso seja menor, retorna False imediatamente, pois não é possível continuar. Se conseguir destruir, a massa é aumentada pelo valor do asteroide, permitindo enfrentar os próximos maiores. Ao final, se todos forem destruídos com sucesso, a função retorna True.

from typing import List


def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
    asteroids.sort()
    for x in asteroids:
        if mass < x:
            return False
        mass += x

    return True


mass = 10
asteroids = [3, 9, 19, 5, 21]
print(asteroidsDestroyed(None, mass, asteroids))