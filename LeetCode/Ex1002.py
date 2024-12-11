def commonChars(words):
    output = list(words[0])

    for x in range(1, len(words)):
        aux = list(words[x])
        temp = []
        for y in aux:
            if y in output:
                output.remove(y)  
                temp.append(y)  
        output = temp
        
    return output


words = ["bella", "label", "roller"]
print(commonChars(words))
