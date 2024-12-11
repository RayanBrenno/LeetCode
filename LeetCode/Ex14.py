def bla(list):
    
    short = min(list, key =len)

    for x in strs:
        for y in range(len(short)):
            print(short)
            if x[y] != short[y]:
                short = short[:y]
                break

    return short

strs = ["flower","flow","flight"]
print(bla(strs))