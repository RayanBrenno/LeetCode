# Esse exercício verifica se todos os '1' da string aparecem em um único bloco contínuo. A lógica é simples: se existir a sequência "01", significa que apareceu um 0 depois de um 1, e depois possivelmente outro 1, o que indicaria mais de um segmento de 1s. Então o código apenas retorna se "01" não está presente na string. Se não existir "01", quer dizer que todos os 1s estão juntos, e a função retorna True; caso contrário, retorna False.

def checkOnesSegment(self, s: str) -> bool:
    return "01" not in s
    
s = "011111111111"
print(checkOnesSegment(None, s))
