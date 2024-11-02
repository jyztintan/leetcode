class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        prev = ''
        # Check that each last char of a word equals the first char of the next word
        for word in sentence.split(' '):
            if prev and prev != word[0]:
                return False
            prev = word[-1]
        # Check that first char matches last char
        return sentence[0] == sentence[-1]