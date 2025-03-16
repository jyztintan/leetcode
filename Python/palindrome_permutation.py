class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        freq = Counter(s)
        count = 0
        for c in freq:
            if freq[c] % 2:
                count += 1
        return count <= 1
