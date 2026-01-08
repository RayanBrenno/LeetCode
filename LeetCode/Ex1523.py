# Conta a quantidade de números ímpares em um intervalo fechado [low, high].

def countOdds(low: int, high: int) -> int:
    return (high - low) // 2 + (1 if low % 2 == 1 or high % 2 == 1 else 0)


low = 3 
high = 7
print(countOdds(low, high))     


