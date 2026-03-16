# O algoritmo gera todas as happy strings de tamanho n usando backtracking. Uma happy string é formada apenas pelos caracteres "a", "b" e "c", com a restrição de que não podem existir dois caracteres iguais consecutivos. A função começa chamando um backtracking que constrói as strings caractere por caractere. A cada passo, tenta adicionar "a", "b" ou "c", mas pula a opção caso seja igual ao último caractere já colocado, garantindo que não haja repetição consecutiva. Quando a string atinge tamanho n, ela é adicionada à lista de resultados. Depois que todas as combinações válidas são geradas, o algoritmo verifica se existem pelo menos k strings; se não existir, retorna "". Caso contrário, retorna a k-ésima string da lista (considerando indexação começando em 1).

class Solution:

    def getHappyString(self, n: int, k: int) -> str:
        current_string = ""
        arr_strings = []
        self.backtrack(n, current_string, arr_strings)
        if len(arr_strings) < k:
            return ""

        return arr_strings[k-1]

    def backtrack(self, n, current_string, arr_strings):
        if len(current_string) == n:
            arr_strings.append(current_string)
            return
        for aux in ["a", "b", "c"]:
            if len(current_string) > 0 and current_string[-1] == aux:
                continue

            self.backtrack(n, current_string + aux, arr_strings)
        
        
n = 3
k = 9
print(Solution().getHappyString(n, k))
