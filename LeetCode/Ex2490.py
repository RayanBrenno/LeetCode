def isCircularSentence(sentence):

    sentence = sentence.split(" ")
    for x in range(len(sentence)):
        if x+1 == len(sentence):
            return True if sentence[x][-1] == sentence[0][0] else False
        if sentence[x][-1] != sentence[x+1][0]:
            break
    return False


sentence = "leetcode exercises sound delightful"
print(isCircularSentence(sentence))
