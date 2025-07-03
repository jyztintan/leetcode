class Solution:
    def kthCharacter(self, k: int) -> str:
        word = ["a"]
        while len(word) < k:
            new_word = []
            for c in word:
                new_word.append(chr(((ord(c) + 1 - ord('a')) % 26) + ord('a')))
            word.extend(new_word)
        return word[k - 1]
