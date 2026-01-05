from typing import Counter


def canConstruct(ransomNote: str, magazine: str) -> bool:
    if len(ransomNote) > len(magazine):
        return False
    
    count = Counter(ransomNote)

    for char, num in count.items():
        if num > magazine.count(char):
            return False

    return True


ransomNote = "aa"
magazine = "aab"
print(canConstruct(ransomNote, magazine))
