from itertools import product 

def letterCombinations(digits):
    dic = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }
    
    if len(digits) == 0:
        return ""

    if len(digits) == 1:
        return dic.get(digits)

    arrDig = []
    for x in digits:
        arrDig.append(dic.get(x))
        
    
    combinations = [''.join(combo) for combo in product(*arrDig)]

    return combinations

print(letterCombinations("2345"))
