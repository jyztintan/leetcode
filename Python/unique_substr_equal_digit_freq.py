class TrieNode:
    def __init__(self):
        self.children = {}
        self.visited = False

class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        trie = TrieNode()
        n = len(s)

        valid_substr = 0
        for start, c in enumerate(s):
            curr = trie
            digit_freq = [0] * 10
            unique_digits = 0
            max_digit_freq = 0

            for end in range(start, n):
                curr_digit = int(s[end])
                if digit_freq[curr_digit] == 0:
                    unique_digits += 1
                digit_freq[curr_digit] += 1
                max_digit_freq = max(max_digit_freq, digit_freq[curr_digit])

                if curr_digit not in curr.children:
                    curr.children[curr_digit] = TrieNode()
                curr = curr.children[curr_digit]

                if (unique_digits * max_digit_freq == end - start + 1 and not curr.visited):
                    valid_substr += 1
                    curr.visited = True
        return valid_substr
