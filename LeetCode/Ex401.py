# Esse código gera todos os horários possíveis de um relógio binário. Ele percorre todas as horas de 0 a 11 e todos os minutos de 0 a 59, converte cada um para binário e conta quantos bits 1 existem em cada parte. Se a soma dos bits ligados da hora e dos minutos for igual a turnedOn, ele adiciona esse horário na resposta, formatando os minutos com zero à esquerda quando necessário. No final, retorna a lista com todos os horários que possuem exatamente aquela quantidade de LEDs acesos.

from typing import List

def readBinaryWatch(self, turnedOn: int) -> List[str]:
    ans = []
    for i in range(12):
        for j in range(60):
            if (bin(i).count('1') + bin(j).count('1')) == turnedOn:
                ans.append(str(i) + ":" + (str(j) if j > 9 else "0" + str(j)))
    return ans

turnedOn = 1
print(readBinaryWatch(None, turnedOn))