
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(' ')
        words = list(map(set, words))
        brokenLetters = set(brokenLetters)
        count = 0
        for word in words:
            if len(word.intersection(brokenLetters)) == 0:
                count += 1
        return count
