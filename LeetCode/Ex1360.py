# Converte as duas strings em objetos date com fromisoformat(), subtrai um do outro (o resultado é um timedelta) e pega o .days. O abs() garante que não importa a ordem das datas.

from datetime import date


def daysBetweenDates(self, date1: str, date2: str) -> int:
    d1 = date.fromisoformat(date1)
    d2 = date.fromisoformat(date2)

    return abs((d2 - d1).days)


date1 = "2019-06-29"
date2 = "2019-06-30"
print(daysBetweenDates(date1, date2))