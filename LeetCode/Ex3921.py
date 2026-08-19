# A solução percorre os eventos acumulando a pontuação em ans, onde ans[0] representa os pontos do jogador e ans[1] a quantidade de vitórias. A cada "W", incrementa as vitórias e encerra o loop quando chega a 10. Para os demais eventos, soma 1 ponto quando o evento é "WD" ou "NB", e nos outros casos converte o valor para inteiro e adiciona à pontuação. No final, retorna a lista com a pontuação e o número de vitórias.

from typing import List

def scoreValidator(self, events: List[str]) -> List[int]:
        ans = [0, 0]
        for x in events:
            if x == "W":
                ans[1] += 1
                if ans[1] >= 10:
                    break
            else:
                ans[0] += 1 if x == "WD" or x == "NB" else int(x)
            
        return ans
    
    
events = ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "WD"]
print(scoreValidator(None, events))