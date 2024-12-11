def decrypt(code, k):
    if k == 0:
        return [0]*len(code)

    elif k > 0:
        res = []
        for x in range(len(code)):
            aux = x + 1
            value = 0
            for x in range(k):
                if aux > len(code)-1:
                    aux = 0
                value += code[aux]
                aux += 1
            res.append(value)
        return res

    else:
        res = [0]*len(code)
        for x in range(len(code)-1, -1, -1):
            aux = x - 1
            value = 0
            for _ in range(abs(k)):
                if aux < 0:
                    aux = len(code) - 1
                value += code[aux]
                aux -= 1

            res[x] = value

        return res


code = [2, 4, 9, 3]
k = -2
print(decrypt(code, k))
