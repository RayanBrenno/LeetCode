# Usa 1971-01-01 (Friday) como base, soma os dias de todos os anos anteriores (365 ou 366 se bissexto), soma os dias dos meses anteriores no ano atual (fevereiro = 29 se bissexto), soma o dia atual e usa (count-1) % 7 pra alinhar com o array de dias da semana

def dayOfTheWeek(self, day: int, month: int, year: int) -> str:

    def isLeap(year):
        return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

    count = day
    days_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ans = ["Friday", "Saturday", "Sunday", "Monday",
           "Tuesday", "Wednesday", "Thursday"]

    for x in range(1971, year):
        count += 366 if isLeap(x) else 365
    for x in range(month-1):
        count += 29 if x == 1 and isLeap(year) else days_month[x]

    return ans[(count-1) % 7]

# Example usage:
print(dayOfTheWeek(None, 31, 8, 2019))  # Output: "Saturday"
