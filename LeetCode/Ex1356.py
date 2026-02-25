# A função recebe a lista de números e usa o sorted para ordenar tudo de uma vez. A regra de ordenação é definida pelo key, que para cada número cria uma tupla com dois valores: primeiro a quantidade de bits 1 na representação binária dele (bin(x).count('1')) e depois o próprio número. O Python então compara essas tuplas ao ordenar, olhando primeiro a quantidade de bits 1; quem tiver menos vem antes. Se dois números tiverem a mesma quantidade de bits 1, ele desempata usando o próprio valor do número em ordem crescente. No final ele retorna a nova lista já organizada seguindo exatamente esse critério.

def sortByBits(arr):
    
    sorted_arr = sorted(arr, key=lambda x: (bin(x).count('1'), x))
    return sorted_arr


    # for x in range(len(arr)-1):
    #     for y in range(len(arr)-1):
    #         if (arr[y]>arr[y+1] and bin(arr[y]).count('1') == bin(arr[y+1]).count('1')) or bin(arr[y]).count('1') > bin(arr[y+1]).count('1'):
    #             arr[y], arr[y + 1] = arr[y + 1], arr[y]

    # return arr
arr = [0,1,2,3,4,5,6,7,8]
print(sortByBits(arr))
