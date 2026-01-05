from typing import Counter, List


def countCharacters(words: List[str], chars: str) -> int:
    res = 0

    for word in words:
        for char in word:
            if word.count(char) > chars.count(char):
                break
        else:
            res += len(word)

    return res


words = ["skwgxuuuumkfurejmqrbipvlavdrozjyxhagbwetabjwevfsegqfpllgafm","ufvpzzgpswnk","tcouxmlrnfyoxvkeglchhryykmdvgvdxpookbtiyhuthoqsnqbowewpfgbcy","qwpttmxzazkkfqqtrnkaejifligdvgnyvtmppjbkeuqryxzqyegttvhzolpztvigxygzvsppurijaekb","vbtvbheurzbglzljczmziitkbmtoybiwhoyfrsxvfveaxchebjdzdnnispzwbrgrbcdaistps"]
chars = "avyteswqppomeojxoybotzriuvxolmllevluauwb"
print(countCharacters(words, chars))
