class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        contains_vowel = False
        contains_consonant = False
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for c in word:
            if not c.isalnum():
                return False
            if c.lower() in vowels:
                contains_vowel = True
            elif c.isalpha():
                contains_consonant = True
        return contains_vowel and contains_consonant
