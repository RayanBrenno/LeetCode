def reverseWords(s):

    s = s.split(" ")
    for x in range(len(s)):
        s[x] = s[x][::-1]
    return " ".join(s)


s = "Let's take LeetCode contest"
print(reverseWords(s))
