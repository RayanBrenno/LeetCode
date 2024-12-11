def isPrefixOfWord(sentence, searchWord):
    sentence = sentence.split(" ")
    for index, word in enumerate(sentence):
        if word.startswith(searchWord):
            return index+1
    return -1


sentence = "thispro problem is an easy problem"
searchWord = "pro"
print(isPrefixOfWord(sentence, searchWord))
