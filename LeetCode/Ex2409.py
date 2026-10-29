# A ideia foi transformar cada data em um número representando o dia do ano, somando os dias dos meses anteriores e o dia atual. Depois disso, basta encontrar onde os dois intervalos se sobrepõem: o início da interseção é a maior data de chegada, e o fim é a menor data de saída. Se houver sobreposição, retorna a quantidade de dias (somando 1 porque as datas são inclusivas); caso contrário, retorna 0.
    

def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def convert(date):
        month, day = date.split("-")
        return sum(months[:int(month) - 1]) + int(day)

    alice = [convert(arriveAlice), convert(leaveAlice)]
    bob = [convert(arriveBob), convert(leaveBob)]

    return max(0, min(alice[1], bob[1]) - max(alice[0], bob[0]) + 1)


leaveAlice = "08-15"
arriveAlice = "08-01"
leaveBob = "08-18"
arriveBob = "08-10"
print(countDaysTogether(None, arriveAlice, leaveAlice, arriveBob, leaveBob))