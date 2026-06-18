# A função verifica o valor de timer para determinar o estado de um semáforo. Se o tempo for 0, retorna "Green". Se for exatamente 30, retorna "Orange". Se estiver entre 31 e 90 (inclusive), retorna "Red". Para qualquer outro valor, considera a entrada inválida e retorna "Invalid".

def trafficSignal(self, timer: int) -> str:
    if timer == 0:
        return "Green"
    elif timer == 30:
        return "Orange"
    elif 30 < timer <= 90:
        return "Red"
    else:
        return "Invalid"


timer = 30
print(trafficSignal(None, timer))
