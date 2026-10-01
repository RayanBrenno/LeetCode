# O código percorre a matriz somando os elementos das duas diagonais. Para isso, utiliza dois índices, left e right, que começam nas extremidades da matriz e avançam em direções opostas a cada linha. O if left != right evita que o elemento central seja somado duas vezes em matrizes de tamanho ímpar. Ao final, o valor acumulado em ans representa a soma das duas diagonais.

def diagonalSum(self, mat: list[list[int]]) -> int:
    left, right = 0, len(mat) - 1
    ans = 0
    for x in range(right + 1):
        if left != right:
            ans += mat[x][left]
        ans += mat[x][right]
        left += 1
        right -= 1

    return ans


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(diagonalSum(None, mat))
