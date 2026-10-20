# A ideia principal é formar inicialmente o máximo de hambúrgueres small possível, considerando que cada um utiliza 2 fatias de tomate e 1 de queijo. Depois, calculamos quantas fatias de tomate sobram em relação a essa quantidade e usamos esse excedente para transformar os small em jumbo, já que cada jumbo precisa de 2 fatias de tomate a mais. Por fim, verificamos se as quantidades são válidas e se todos os ingredientes foram utilizados.


def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> list[int]:
    jumbo = (tomatoSlices - 2 * cheeseSlices) // 2
    small = cheeseSlices - jumbo

    if jumbo < 0 or small < 0 or 4 * jumbo + 2 * small != tomatoSlices:
        return []

    return [jumbo, small]


tomatoSlices = 16
cheeseSlices = 7
print(numOfBurgers(None, tomatoSlices, cheeseSlices))
