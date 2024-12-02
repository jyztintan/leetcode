class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split(" ")
        for i, word in enumerate(sentence):
            if word.startswith(searchWord):
                return i + 1
        return - 1
