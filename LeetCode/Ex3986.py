# A implementação converte os horários inicial e final em segundos, multiplicando as horas por 3600 e os minutos por 60, somando os segundos restantes. Depois, basta subtrair o total de segundos do horário inicial do horário final para obter o tempo decorrido.


def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
    h1, m1, s1 = map(int, startTime.split(':'))
    h2, m2, s2 = map(int, endTime.split(':'))

    start = h1 * 3600 + m1 * 60 + s1
    end = h2 * 3600 + m2 * 60 + s2

    return end - start


startTime = "12:30:15"
endTime = "14:45:30"
print(secondsBetweenTimes(None, startTime, endTime))  # Output: 8130
