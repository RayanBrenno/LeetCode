# Esse exercício calcula a distância total considerando que a cada 5 litros consumidos do tanque principal você pode transferir 1 litro do tanque adicional, e como cada litro rende 10 km, o objetivo é descobrir quantos litros extras realmente podem ser usados. A sacada matemática é perceber que, após o primeiro ciclo de 5 litros, cada novo bônus efetivamente exige apenas 4 litros adicionais do tanque principal, porque o litro ganho ajuda a completar o próximo grupo de 5; por isso o limite estrutural de bônus é dado por (mainTank - 1) // 4. Como também não é possível usar mais litros do que existem no tanque adicional, usamos min((mainTank - 1) // 4, additionalTank) para encontrar o número real de bônus, somamos ao mainTank e multiplicamos tudo por 10 para obter a distância final.

def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
    bonus = min((mainTank - 1) // 4, additionalTank)
    return (mainTank + bonus) * 10


mainTank = 9
additionalTank = 2
print(distanceTraveled(None, mainTank, additionalTank))