class Solution:
    def possibleStringCount(self, word: str) -> int:
        prev = ""
        count = 1 # The case where no mistypes
        for c in word:
            if c == prev:
                count += 1
            prev = c
        return count
