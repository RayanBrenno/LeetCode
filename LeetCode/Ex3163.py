def compressedString(word):

    output = []
    count = 1

    for i in range(1, len(word) + 1):
        if i == len(word) or word[i] != word[i - 1] or count == 9:
            output.append(str(count)+word[i - 1])
            count = 1
        else:
            count += 1

    return ''.join(output)

    """
        cont = 1
        output = ""
        x = 0
        while x < len(word):

            if x == len(word)-1:
                output = output + str(cont) + word[x]

            else:
                if x+1 < len(word) and word[x] == word[x+1]:
                    cont += 1
                    if cont == 10:
                        output = output + str(cont-1) + word[x]
                        cont = 1
                else:
                    output = output + str(cont) + word[x]
                    cont = 1

            x += 1

        return output
    """


word = "abcde"
print(compressedString(word))

word = "aaaaaaaaaaaaaabb"
print(compressedString(word))
