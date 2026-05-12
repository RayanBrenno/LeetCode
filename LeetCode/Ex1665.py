# A ideia do exercício é encontrar a energia inicial mínima para completar todas as tarefas. O algoritmo ordena as tarefas pela diferença entre energia mínima necessária e energia gasta (em ordem crescente), depois itera pelas tarefas acumulando a energia necessária com  max(energia_atual + energia_gasta, energia_minima). O resultado final é a energia inicial que você precisa.

def minimumEffort(tasks):
    tasks.sort(key=lambda x: x[1] - x[0])
    ans = 0
    for actual, minimum in tasks:
        ans = max(ans + actual, minimum)
    
    return ans

tasks = [[1,3], [2,4], [10,11], [10,3], [5,8]]
print(minimumEffort(tasks))  # Output: 8