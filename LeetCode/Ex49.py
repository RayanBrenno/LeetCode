from collections import defaultdict

def groupAnagrams(strs):
    anagrams = defaultdict(list)

    for words in strs:
        aux = ''.join(sorted(words))
        anagrams[aux].append(words)

    return list(anagrams.values())

    """
    output = []
    x = 0
    while x < len(strs):
        arrAux = [strs[x]]
        aux = sorted(list(strs[x]))
        for y in range(len(strs)-1, x, -1):
            if aux == sorted(list(strs[y])):
                arrAux.append(strs[y])
                strs.pop(y)
        output.append(arrAux)
        x += 1
    return output
    """


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
