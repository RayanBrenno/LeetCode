from collections import defaultdict


def maximumLength(s):

    dictionary = defaultdict(int)
    for x in range(len(s)):
        for y in range(len(s)-x):
            text = s[y:y+x+1]
            dictionary[text] += 1

    longest = -1
    dictionary = sorted(dictionary.items(), key=lambda x:x[1], reverse = True)
    print(dictionary)
    for string, rep in dictionary:
        if rep < 3:
            break
        longest = max(longest, len(string))

    return longest


s = "cccerrrecdcdccedecdcccddeeeddcdcddedccdceeedccecde"
print(maximumLength(s))
