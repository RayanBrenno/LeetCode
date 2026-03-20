#Esse código resolve o problema usando uma observação matemática interessante: embora a situação pareça complexa (com várias pessoas escolhendo assentos de forma aleatória), o resultado final acaba sendo bem simples. Se há apenas uma pessoa (n == 1), ela obviamente senta no próprio lugar, então a probabilidade é 1.0. Porém, para qualquer número maior de pessoas, a probabilidade de a última pessoa sentar no seu próprio assento sempre será 0.5. Isso acontece porque, ao longo do processo, as escolhas aleatórias acabam reduzindo o problema a duas possibilidades igualmente prováveis no final: ou o último assento disponível é o correto, ou é o assento da primeira pessoa. Por isso, o código retorna diretamente 0.5 para qualquer n > 1, sem precisar simular nada.

def nthPersonGetsNthSeat(self, n: int) -> float:
    return 1.0 if n == 1 else 0.5


n = 3
print(nthPersonGetsNthSeat(None, n))