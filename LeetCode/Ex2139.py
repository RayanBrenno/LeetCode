# Enquanto o target for maior que 1, ele faz o seguinte: se ainda pode usar divisões (maxDoubles > 0) e o número for par, ele divide por 2 e diminui a quantidade de doubles disponíveis. Se o número for ímpar, ele subtrai 1 (porque não dá pra dividir ímpar). Se acabar o maxDoubles, ele simplesmente retorna o que já contou mais target - 1, porque daí só resta ir diminuindo de 1 em 1 até chegar em 1.

def minMoves(self, target: int, maxDoubles: int) -> int:
    ans = 0
    while target > 1:
        if maxDoubles == 0:
            return ans + target - 1
        elif maxDoubles > 0 and target % 2 == 0:
            target //= 2
            maxDoubles -= 1
        else:
            target -= 1
        ans += 1
        
        # if maxDoubles > 0:
        #     if target % 2 == 0:
        #         target //= 2
        #         maxDoubles -= 1
        #     else:
        #         target -= 1
        #     ans += 1
        # else:
        #     return ans + target - 1

    return ans


target = 19
maxDoubles = 2
print(minMoves(None, target, maxDoubles))