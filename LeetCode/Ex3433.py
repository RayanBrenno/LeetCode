# Primeiro a gente ordena os eventos pelo tempo e, em caso de empate, coloca os eventos ***"OFFLINE" antes de "MESSAGE"***, porque no problema quem fica offline em um timestamp já deve ser considerado offline para mensagens naquele mesmo instante. Depois criamos duas listas: mentions, que guarda quantas menções cada usuário recebeu, e next_online_time, que indica até que momento cada usuário permanece offline (ou seja, ele só está online quando next_online_time[i] <= tempo_atual).
# Percorremos os eventos em ordem. Quando o evento é "OFFLINE", marcamos que o usuário ficará offline até tempo_atual + 60. Quando o evento é "MESSAGE", tratamos três casos: se for "ALL", incrementamos a contagem de todos os usuários; se for "HERE", incrementamos apenas daqueles que estão online no momento; e se for uma lista de ids ("idX idY"), incrementamos diretamente os usuários mencionados, independentemente de estarem online ou offline.

from typing import List


def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:

    events.sort(key=lambda x: (int(x[1]), x[0] == "MESSAGE"))
    mentions = [0] * numberOfUsers
    next_online_time = [0] * numberOfUsers

    for event in events:
        cur_time = int(event[1])

        if event[0] == "MESSAGE":

            if event[2] == "ALL":
                for i in range(numberOfUsers):
                    mentions[i] += 1

            elif event[2] == "HERE":
                for i in range(numberOfUsers):
                    if next_online_time[i] <= cur_time:
                        mentions[i] += 1

            else:
                for idx in event[2].split():
                    user_id = int(idx[2:])
                    mentions[user_id] += 1

        else:
            user_id = int(event[2])
            next_online_time[user_id] = cur_time + 60

    return mentions


numberOfUsers = 3
events = [["MESSAGE", "1", "id0 id1"], ["MESSAGE", "5", "id2"],
          ["MESSAGE", "6", "ALL"], ["OFFLINE", "5", "2"]]
print(countMentions(None, numberOfUsers, events))
