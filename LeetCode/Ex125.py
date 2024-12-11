def isPalindrome(s):
    s = ''.join(char for char in s if char.isalnum()).upper()
    return s == s[::-1]


s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
