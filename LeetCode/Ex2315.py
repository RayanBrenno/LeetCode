# Divide a string pelo |, resultando em segmentos alternados entre "fora" e "dentro" dos pipes. O flag controla qual segmento está sendo processado — começa como True (fora) e alterna a cada iteração. Só acumula a contagem de * nos segmentos onde flag é True, ignorando o conteúdo entre pares de pipes. Retorna o total de asteriscos fora dos delimitadores.

def countAsterisks(self, s: str) -> int:
    # ans = 0
    # count = 0
    # for x in s:
    #     if x == '|':
    #         count += 1
    #     elif count % 2 == 0 and x == '*':
    #         ans += 1
    
    # return ans 
    
    aux = s.split("|")
    flag = True
    ans = 0
    for x in aux:
        if flag:
            ans += x.count("*")
            flag = False
        else:
            flag = True

    return ans


s = "l|*e*et|c**o|*de|"
print(countAsterisks(None, s))