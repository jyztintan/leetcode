class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        palindromes = 0

        for letter in letters:
            left_most, right_most = s.index(letter), s.rindex(letter)
            possible_middle = set(s[left_most + 1: right_most])
            palindromes += len(possible_middle)

        return palindromes
